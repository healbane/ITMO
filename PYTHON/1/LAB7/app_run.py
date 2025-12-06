import logging
import io
from logtools import trace
from cbr_rates import get_currencies
from solver_quad import solve_quadratic

# ============================================================
# 1. Демонстрация логгера с API Центробанка
# ============================================================

print("=== Демонстрация работы API ЦБ РФ ===")

@trace()
def demo_usd():
    return get_currencies(["USD"])

try:
    print("USD:", demo_usd())
except Exception as e:
    print("Ошибка:", e)


# Логирование в файл
file_logger = logging.getLogger("currency_file")
file_logger.setLevel(logging.INFO)

if not file_logger.handlers:
    handler = logging.FileHandler("currency.log", encoding="utf-8")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    file_logger.addHandler(handler)

@trace(handle=file_logger)
def demo_usd_eur():
    return get_currencies(["USD", "EUR"])

try:
    print("USD + EUR:", demo_usd_eur())
except Exception as e:
    print("Ошибка:", e)


# ============================================================
# 2. Демонстрация квадратных уравнений
# ============================================================

print("\n=== Решение квадратных уравнений с логированием ===")

# Настройка отдельного логгера для квадратных уравнений
quad_logger = logging.getLogger("quad_logger")
quad_logger.setLevel(logging.DEBUG)

if not quad_logger.handlers:
    handler = logging.FileHandler("quad.log", encoding="utf-8")
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    quad_logger.addHandler(handler)


@trace(handle=quad_logger)
def demo_quad(a, b, c):
    return solve_quadratic(a, b, c)


print("→ Два корня:", demo_quad(1, -5, 6))
print("→ Один корень:", demo_quad(1, -4, 4))

try:
    print("→ Нет корней:", demo_quad(1, 0, 1))
except Exception as e:
    print("→ Ошибка: нет корней:", e)

try:
    demo_quad(0, 2, 3)
except Exception as e:
    print("→ Ошибка a=0:", e)

try:
    demo_quad("abc", 2, 3)
except Exception as e:
    print("→ Ошибка: неправильный тип:", e)



print("\nГотово. Все логи записаны в currency.log и quad.log")
