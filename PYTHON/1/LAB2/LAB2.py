from typing import List, Tuple


def guess_number(target: int, numbers_range: List[int], method: str = "binary") -> Tuple[int, int]:
    """
    Угадывает число в заданном диапазоне с использованием указанного метода.

    Args:
        target (int): Число, которое нужно угадать
        numbers_range (List[int]): Диапазон чисел для поиска
        method (str): Метод угадывания - "binary" или "linear"

    Returns:
        Tuple[int, int]: Кортеж (угаданное_число, количество_попыток)

    Raises:
        ValueError: Если target не входит в диапазон
    """
    if not numbers_range:
        raise ValueError("Диапазон чисел не может быть пустым")

    if target not in numbers_range:
        raise ValueError(f"Число {target} не входит в диапазон")

    # Автоматически исправляем неверный метод (пусть будет бинарный по умолчанию)
    if method not in ["binary", "linear"]:
        method = "binary"

    if method == "binary" and numbers_range != sorted(numbers_range):
        raise ValueError("Для бинарного поиска диапазон должен быть отсортирован")

    if method == "binary":
        return _binary_search(target, numbers_range)
    else:
        return _linear_search(target, numbers_range)


def _binary_search(target: int, numbers: List[int]) -> Tuple[int, int]:
    """
    Реализация бинарного поиска для угадывания числа.

    Args:
        target (int): Число для поиска
        numbers (List[int]): Отсортированный список чисел

    Returns:
        Tuple[int, int]: (найденное_число, количество_попыток)
    """
    attempts = 0
    left, right = 0, len(numbers) - 1

    while left <= right:
        attempts += 1
        mid = (left + right) // 2
        guess = numbers[mid]

        if guess == target:
            return guess, attempts
        elif guess < target:
            left = mid + 1
        else:
            right = mid - 1

    # Эта точка недостижима благодаря проверкам в guess_number, но пусть будет
    raise RuntimeError("Алгоритм бинарного поиска не нашел число, хотя оно должно быть в диапазоне")


def _linear_search(target: int, numbers: List[int]) -> Tuple[int, int]:
    """
    Реализация линейного поиска для угадывания числа.

    Args:
        target (int): Число для поиска
        numbers (List[int]): Список чисел

    Returns:
        Tuple[int, int]: (найденное_число, количество_попыток)
    """
    attempts = 0

    for number in numbers:
        attempts += 1
        if number == target:
            return number, attempts

    # Эта точка недостижима благодаря проверкам в guess_number, но пусть будет
    raise RuntimeError("Алгоритм линейного поиска не нашел число, хотя оно должно быть в диапазоне")


def input_helper() -> Tuple[int, List[int], str]:
    """
    Вспомогательная функция для ввода данных с клавиатуры.

    Returns:
        Tuple[int, List[int], str]: (target, numbers_range, method)

    Raises:
        ValueError: Если диапазон некорректен
    """
    try:
        start = int(input("Введите начало диапазона: "))
        end = int(input("Введите конец диапазона: "))

        # Проверка корректности заданного диапазона
        if start > end:
            raise ValueError("Начало диапазона не может быть больше конца")

        target = int(input("Введите число для угадывания: "))
        method_input = input("Выберите метод (бинарный/линейный): ").strip().lower()

        # Преобразование метода
        if method_input == "бинарный":
            method = "binary"
        elif method_input == "линейный":
            method = "linear"
        else:
            print("Неверный метод, используется бинарный по умолчанию")
            method = "binary"

        numbers_range = list(range(start, end + 1))

        # Дополнительная проверка, что наш target в диапазоне
        if target < start or target > end:
            raise ValueError(f"Число {target} не входит в диапазон [{start}, {end}]")

        return target, numbers_range, method

    except ValueError as e:
        raise ValueError(f"Некорректный ввод данных: {e}")
    

def main():
    """Основная функция для запуска игры"""
    print("Игра 'Угадай число'")

    try:
        target, numbers_range, method = input_helper()

        result, attempts = guess_number(target, numbers_range, method)

        print("\nРезультат:")
        print(f"Загаданное число: {result}")
        print(f"Количество попыток: {attempts}")

        method_name = "бинарный" if method == "binary" else "линейный"
        print(f"Использованный метод: {method_name}")

    except ValueError as e:
        print(f"Ошибка: {e}")
    except KeyboardInterrupt:
        print("Игра прервана")

if __name__ == "__main__":
    main()
