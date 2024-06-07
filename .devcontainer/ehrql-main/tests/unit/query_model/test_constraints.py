from datetime import date

from ehrql.tables import Constraint


def test_categorical_validation():
    c = Constraint.Categorical((1, "a"))
    assert c.validate("a")
    assert c.validate(None)
    assert not c.validate("")
    assert not c.validate("b")


def test_not_null_validation():
    c = Constraint.NotNull()
    assert c.validate(1)
    assert not c.validate(None)


def test_unique_validation():
    c = Constraint.Unique()
    assert c.validate(1)


def test_first_of_month_validation():
    c = Constraint.FirstOfMonth()
    assert c.validate(date(2024, 1, 1))
    assert c.validate(None)
    assert not c.validate(date(2024, 1, 2))


def test_regex_validation():
    c = Constraint.Regex("E020[0-9]{5}")
    assert c.validate("E02012345")
    assert c.validate(None)
    assert not c.validate("")
    assert not c.validate("E020")


def test_closed_range_validation():
    c = Constraint.ClosedRange(1, 3)
    assert c.validate(2)
    assert c.validate(None)
    assert not c.validate(0)
    assert not c.validate(4)
