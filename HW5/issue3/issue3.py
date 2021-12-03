import unittest
from one_hot_encoder import fit_transform

class TestFitTransformFunction(unittest.TestCase):
    def test_cities(self):
        #Тест по типу исходного кода
        self.assertEqual(fit_transform(['Abu-Dahbi', 'Las-Vegas', 'Abu-Dahbi']),
                         [('Abu-Dahbi', [0, 1]), ('Las-Vegas', [1, 0]), ('Abu-Dahbi', [0, 1])])
        
        
    def test_sueta(self):
        self.assertEqual(fit_transform([1212, 323 ,5],
                                       [(1212, [0, 0, 1]), (323, [0, 1, 0]), (5, [1, 0, 0])])

    def test_noargs(self):
        # Тест на пустую функцию
        with self.assertRaises(TypeError):
            fit_transform()
        # TypeError
        # TypeError: expected at least 1 arguments, got 0
    

    def test_empty_input(self):
        # Не ввели ни один город в открывшееся меню
        self.assertEqual(fit_transform([]), [])

    def test_sueta_nesueta(self):
        # Тест на несповпадение с некорректным ответом
        self.assertNotEqual(fit_transform([1212, 323 ,5]),
                           [(1212, [0, 0, 2]), (323, [0, 1, 0]), (5, [1, 0, 0])])



if __name__ == '__main__':
    unittest.main()
