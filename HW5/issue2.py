import pytest
from morse import decode


# Запустим модуль параметрайзер, который получает на вход 2 значения
# Декодер  - как фукнция переведёт наш "input()"
# Ожидаемое значение - то, что должно быть на самом деле
@pytest.mark.parametrize('morse_encode, expected_result', [
                                                            ('-.-. .... .- -. -.. .-', 'CHANDA'),
                                                            ('... --- ...', 'SOS'),
                                                            ('..- ... .-', 'USA')
                                                                                    ])


def test_morse_decoding(morse_encode,expected_result):
    assert decode(morse_encode) == expected_result
