from typing import Tuple
from logtools import trace, file_logger


@trace(handle=file_logger)  # можно заменить на sys.stdout или другой handle
def solve_quadratic(a: float, b: float, c: float) -> Tuple[float, float]:
    """
    Решение квадратного уравнения ax^2 + bx + c = 0.
    Возвращает кортеж из двух корней (могут совпадать).
    Выбрасывает исключения при некорректных входных данных.
    """

    # Проверка типов данных
    for value in (a, b, c):
        if not isinstance(value, (int, float)):
            raise TypeError("Коэффициенты должны быть числами")

    if a == 0:
        raise ValueError("Коэффициент 'a' не может быть равен нулю в квадратном уравнении")

    # Вычисление дискриминанта
    d = b ** 2 - 4 * a * c

    if d < 0:
        raise ValueError("Дискриминант меньше нуля — корней нет")

    sqrt_d = d ** 0.5
    x1 = (-b + sqrt_d) / (2 * a)
    x2 = (-b - sqrt_d) / (2 * a)

    return x1, x2
