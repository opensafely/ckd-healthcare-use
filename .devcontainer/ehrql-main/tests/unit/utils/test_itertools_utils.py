import pytest

from ehrql.utils.itertools_utils import eager_iterator


def test_eager_iterator():
    results = eager_iterator(iter([0, 1, 2]))
    assert list(results) == [0, 1, 2]


def test_eager_iterator_works_on_empty_iterators():
    results = eager_iterator(iter([]))
    assert list(results) == []


def test_eager_iterator_triggers_errors_early():
    def generator_with_error():
        raise ValueError("fail")
        yield  # pragma: no cover

    results = generator_with_error()
    with pytest.raises(ValueError, match="^fail$"):
        eager_iterator(results)


def test_eager_iterator_still_mostly_lazy():
    i = iter(range(3))
    assert i.__length_hint__() == 3
    # Check that making it eager consumes exactly one item
    eager = eager_iterator(i)
    assert i.__length_hint__() == 2
    # Check that consuming the eager iterator consumes the rest of the items
    assert list(eager) == [0, 1, 2]
    assert i.__length_hint__() == 0
