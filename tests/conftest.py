import pytest


@pytest.fixture
def set_up():
    print("Вход в систему выполнен")
    yield
    print("Выход из системы выполнен")


@pytest.fixture(scope='package')
def some():
    print("Начало теста")
    yield
    print("Полный Конец")

@pytest.fixture(scope='class')
def some_class():
    print("Начало")
    yield
    print("Конец")

