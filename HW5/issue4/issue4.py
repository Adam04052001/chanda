import pytest
from one_hot_encoder import fit_transform


@pytest.mark.parametrize('sample, expecataion',
                         [
                         (['Moscow', 'New York', 'Moscow', 'London'], 
                                                                      [('Moscow', [0, 0, 1]),
                                                                       ('New York', [0, 1, 0]),
                                                                       ('Moscow', [0, 0, 1]),
                                                                       ('London', [1, 0, 0])])
                         ]
                        )


def test_equality(sample, expecataion):
  assert fit_transform(sample) == expectation
    
    
def test_noargs(self):
   # Тест на пустую функцию
   with pytest.raises(TypeError):
     fit_transform()
     # TypeError
     # TypeError: expected at least 1 arguments, got 0
        
def test_inequality(sample, expecataion):
   actual = fit_transform(sample)
   err_msg = f'{actual} != {expecataion}'
   assert actual == expectation, err_msg
    


@pytest.mark.parametrize('sample, expecataion', [
    (
            ['Abu-Dahbi', 'Las-Vegas', 'Abu-Dahbi'],
            ('Las-Vegas', [1, 0])
    )
    
])

def test_notin(sample, expecataion):
    """
    Тест на вхождение правильной кодировки слова в ответ
    :param s: исходный набор строк
    :param exp: ожидаемая кодировка одного из слов
    """
    assert expecataion not in fit_transform(sample)
