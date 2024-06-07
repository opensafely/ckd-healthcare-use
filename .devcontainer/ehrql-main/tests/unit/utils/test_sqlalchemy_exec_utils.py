from unittest import mock

import pytest
import sqlalchemy
from sqlalchemy.exc import OperationalError

from ehrql.utils.sqlalchemy_exec_utils import (
    execute_with_retry_factory,
    fetch_table_in_batches,
)


@pytest.mark.parametrize(
    "table_size,batch_size,expected_query_count",
    [
        (20, 5, 5),  # 4 batches of results, plus one to confirm there are no more
        (20, 6, 4),  # 4th batch will be part empty so we know it's the final one
        (0, 10, 1),  # 1 query to confirm there are no results
        (9, 1, 10),  # a batch size of 1 is obviously silly but it ought to work
    ],
)
def test_fetch_table_in_batches(table_size, batch_size, expected_query_count):
    table_data = [(i, f"foo{i}") for i in range(table_size)]

    # Pretend to be a SQL connection that understands just two forms of query
    class FakeConnection:
        call_count = 0

        def execute(self, query):
            self.call_count += 1
            compiled = query.compile()
            sql = str(compiled).replace("\n", "").strip()
            params = compiled.params

            if sql == "SELECT t.pk, t.foo FROM t ORDER BY t.pk LIMIT :param_1":
                limit = params["param_1"]
                return table_data[:limit]
            elif sql == (
                "SELECT t.pk, t.foo FROM t WHERE t.pk > :pk_1 "
                "ORDER BY t.pk LIMIT :param_1"
            ):
                limit, min_pk = params["param_1"], params["pk_1"]
                return [row for row in table_data if row[0] > min_pk][:limit]
            else:
                assert False, f"Unexpected SQL: {sql}"

    table = sqlalchemy.table(
        "t",
        sqlalchemy.Column("pk"),
        sqlalchemy.Column("foo"),
    )

    connection = FakeConnection()

    results = fetch_table_in_batches(
        connection.execute, table, table.c.pk, batch_size=batch_size
    )
    assert list(results) == table_data
    assert connection.call_count == expected_query_count


ERROR = OperationalError("A bad thing happend", {}, None)


@mock.patch("time.sleep")
def test_execute_with_retry(sleep):
    execute = mock.Mock(side_effect=[ERROR, ERROR, ERROR, "its OK now"])
    execute_with_retry = execute_with_retry_factory(
        execute, max_retries=3, retry_sleep=10, backoff_factor=2
    )
    assert execute_with_retry() == "its OK now"
    assert execute.call_count == 4
    assert sleep.mock_calls == [mock.call(t) for t in [10, 20, 40]]


@mock.patch("time.sleep")
def test_execute_with_retry_exhausted(sleep):
    execute = mock.Mock(side_effect=[ERROR, ERROR, ERROR, ERROR])
    execute_with_retry = execute_with_retry_factory(
        execute, max_retries=3, retry_sleep=10, backoff_factor=2
    )
    with pytest.raises(OperationalError):
        execute_with_retry()
    assert execute.call_count == 4
    assert sleep.mock_calls == [mock.call(t) for t in [10, 20, 40]]
