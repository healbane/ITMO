import unittest
from io import StringIO
from logtools import trace
from solver_quad import solve_quadratic


class TestTraceDecorator(unittest.TestCase):

    def test_trace_success(self):
        """Проверка корректного логирования успешного вызова."""
        log = StringIO()

        @trace(handle=log)
        def add(a, b):
            return a + b

        result = add(2, 3)
        log_content = log.getvalue()

        self.assertEqual(result, 5)
        self.assertIn("INFO: Запуск add(2, 3)", log_content)
        self.assertIn("INFO: add вернула 5", log_content)

    def test_trace_exception(self):
        """Проверка логирования ошибки."""
        log = StringIO()

        @trace(handle=log)
        def bad(x):
            raise ValueError("ошибка!")

        with self.assertRaises(ValueError):
            bad(10)

        log_content = log.getvalue()

        self.assertIn("INFO: Запуск bad(10)", log_content)
        self.assertIn("ERROR: Ошибка в bad: ValueError: ошибка!", log_content)


class TestStringIOLogging(unittest.TestCase):

    def test_logging_stringio(self):
        """Проверка записи в StringIO."""
        log = StringIO()

        @trace(handle=log)
        def fake():
            return {"USD": 100}

        res = fake()
        log_content = log.getvalue()

        self.assertEqual(res, {"USD": 100})
        self.assertIn("INFO: Запуск fake()", log_content)
        self.assertIn("INFO: fake вернула {'USD': 100}", log_content)


class TestQuadraticSolver(unittest.TestCase):

    def test_two_roots(self):
        x1, x2 = solve_quadratic(1, -3, 2)
        self.assertEqual((x1, x2), (2.0, 1.0))

    def test_one_root(self):
        x1, x2 = solve_quadratic(1, 2, 1)
        self.assertEqual((x1, x2), (-1.0, -1.0))

    def test_negative_discriminant(self):
        with self.assertRaises(ValueError):
            solve_quadratic(1, 0, 1)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            solve_quadratic("abc", 1, 1)


if __name__ == "__main__":
    unittest.main()
