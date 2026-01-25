from LAB2 import guess_number
import unittest


class TestGuessNumber(unittest.TestCase):
    """Тесты для функции guess_number"""

    def setUp(self):
        """Подготовка данных для тестов"""
        self.numbers = list(range(1, 101))  # Диапазон 1-100

    def test_binary_search_found(self):
        """Тест бинарного поиска - число найдено"""
        result, attempts = guess_number(42, self.numbers, "binary")
        self.assertEqual(result, 42)
        self.assertLess(attempts, 10)

    def test_linear_search_found(self):
        """Тест линейного поиска - число найдено"""
        result, attempts = guess_number(42, self.numbers, "linear")
        self.assertEqual(result, 42)
        self.assertEqual(attempts, 42)

    def test_number_not_in_range(self):
        """Тест с числом вне диапазона"""
        with self.assertRaises(ValueError):
            guess_number(150, self.numbers, "binary")

    def test_auto_correct_invalid_method(self):
        """Тест автоматического исправления неверного метода"""
        result, attempts = guess_number(42, self.numbers, "invalid")
        self.assertEqual(result, 42)

    def test_first_element(self):
        """Тест первого элемента"""
        result, attempts = guess_number(1, self.numbers, "binary")
        self.assertEqual(result, 1)

    def test_last_element(self):
        """Тест последнего элемента"""
        result, attempts = guess_number(100, self.numbers, "binary")
        self.assertEqual(result, 100)

    def test_small_range(self):
        """Тест с маленьким диапазоном"""
        small_range = list(range(1, 6))
        result, attempts = guess_number(3, small_range, "binary")
        self.assertEqual(result, 3)

    def test_empty_range(self):
        """Тест с пустым диапазоном"""
        with self.assertRaises(ValueError):
            guess_number(1, [], "binary")

    def test_unsorted_range_binary(self):
        """Тест бинарного поиска с несортированным диапазоном"""
        unsorted_range = [5, 2, 8, 1, 9]
        with self.assertRaises(ValueError):
            guess_number(5, unsorted_range, "binary")

if __name__ == "__main__":
    unittest.main(verbosity=2)