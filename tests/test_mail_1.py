import pytest

@pytest.fixture
def set_up():
    print("Вход в систему выполнен!")
    # вводим оператор yield, который позволяет выполнять действия после определённой функции
    yield
    print("Выход из системы выполнен")

def test_sending_mail_1(set_up):
    print("Письмо отправлено")

def test_sending_mail_2(set_up):
    print("Письмо отправлено")

