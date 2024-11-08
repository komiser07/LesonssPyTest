import pytest

@pytest.mark.run(order=4)
def test_week_1():
    print("Wednesday")

@pytest.mark.run(order=6)
def test_week_2():
    print("Friday")

@pytest.mark.run(order=2)
def test_week_3():
    print("Monday")

@pytest.mark.run(order=5)
def test_week_4():
    print("Thursday")

@pytest.mark.run(order=1)
def test_week_5():
    print("Sunday")

@pytest.mark.run(order=3)
def test_week_6():
    print("Tuesday")

@pytest.mark.run(order=7)
def test_week_7():
    print("Saturday")









