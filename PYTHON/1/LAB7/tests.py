import unittest
from unittest.mock import patch
from solver_quad import solve_quadratic
from cbr_rates import get_currencies


# ==========================================================
#   ТЕСТЫ ДЛЯ КВАДРАТНЫХ УРАВНЕНИЙ
# ==========================================================

class TestQuadratic(unittest.TestCase):

    def test_two_roots(self):
        self.assertEqual(solve_quadratic(1, -5, 6), (3.0, 2.0))

    def test_one_root(self):
        self.assertEqual(solve_quadratic(1, -4, 4), (2.0, 2.0))

    def test_no_real_roots(self):
        with self.assertRaises(ValueError):
            solve_quadratic(1, 0, 1)

    def test_a_zero(self):
        with self.assertRaises(ValueError):
            solve_quadratic(0, 2, 3)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            solve_quadratic("abc", 2, 3)


# ==========================================================
#   ТЕСТЫ ДЛЯ API ЦБ РФ (mock запросов)
# ==========================================================

class TestCBR(unittest.TestCase):

    @patch("cbr_rates.requests.get")
    def test_currency_ok(self, mock_get):
        # Подделываем JSON-ответ Центробанка
        mock_get.return_value.json.return_value = {
            "Valute": {
                "USD": {"Value": 76.55},
                "EUR": {"Value": 83.10},
            }
        }
        mock_get.return_value.status_code = 200

        rates = get_currencies(["USD", "EUR"])
        self.assertEqual(rates, {"USD": 76.55, "EUR": 83.10})

    @patch("cbr_rates.requests.get")
    def test_currency_missing_key(self, mock_get):
        mock_get.return_value.json.return_value = {}
        mock_get.return_value.status_code = 200

        with self.assertRaises(KeyError):
            get_currencies(["USD"])

    @patch("cbr_rates.requests.get")
    def test_currency_missing_currency(self, mock_get):
        mock_get.return_value.json.return_value = {"Valute": {}}
        mock_get.return_value.status_code = 200

        with self.assertRaises(KeyError):
            get_currencies(["USD"])

    @patch("cbr_rates.requests.get")
    def test_currency_wrong_type(self, mock_get):
        mock_get.return_value.json.return_value = {
            "Valute": {"USD": {"Value": "wrong"}}
        }
        mock_get.return_value.status_code = 200

        with self.assertRaises(TypeError):
            get_currencies(["USD"])


if __name__ == "__main__":
    unittest.main()
