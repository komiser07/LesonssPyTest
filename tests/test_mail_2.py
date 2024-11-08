# Импортируем библиотеку pytest для тестирования
import pytest

# Определяем фикстуру с именем set_up
@pytest.fixture
def set_up():
    # Выводим сообщение, указывающее, что вход выполнен
    print("Вход в систему выполнен")

# Тестовая функция, без фикстуры set_up
def test_sending_mail_1():
    # Выводим сообщение о том, что письмо отправлено
    print("Письмо отправлено")

# вторая тестовая функция, без фикстуры set_up
def test_sending_mail_2():
    # Выводим сообщение о том, что письмо отправлено
    print("Письмо отправлено")

