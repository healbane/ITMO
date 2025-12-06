import sys
import logging
import functools
from typing import Any, Callable


def trace(func: Callable = None, *, handle=sys.stdout):
    """
    Универсальный логирующий декоратор.
    Поддерживает:
        • обычные потоки (stdout, StringIO) через write()
        • logging.Logger через info()/error()

    Параметры:
        func   — функция, которую оборачиваем
        handle — поток или логгер
    """

    # Проверяем, что передан логгер (у него есть .info() и нет .write())
    def _is_logger(target) -> bool:
        return isinstance(target, logging.Logger)

    is_logger = _is_logger(handle)

    # Функции записи логов в поток или логгер
    def log_info(message: str) -> None:
        if is_logger:
            handle.info(message)
        else:
            handle.write(f"INFO: {message}\n")

    def log_error(message: str) -> None:
        if is_logger:
            handle.error(message)
        else:
            handle.write(f"ERROR: {message}\n")

    def decorator(fn: Callable) -> Callable:
        @functools.wraps(fn)
        def wrapped(*args, **kwargs) -> Any:
            # Формирование сигнатуры вызова
            args_list = [repr(a) for a in args]
            kwargs_list = [f"{k}={repr(v)}" for k, v in kwargs.items()]
            call_repr = ", ".join(args_list + kwargs_list)

            # Логируем старт
            log_info(f"Запуск {fn.__name__}({call_repr})")

            try:
                result = fn(*args, **kwargs)
                log_info(f"{fn.__name__} вернула {repr(result)}")
                return result
            except Exception as exc:  # Логируем любую ошибку
                exc_type = type(exc).__name__
                log_error(f"Ошибка в {fn.__name__}: {exc_type}: {exc}")
                raise

        return wrapped

    # Декоратор вызван как @trace(handle=…)
    if func is None:
        return decorator

    # Декоратор вызван как @trace
    return decorator(func)


# Дополнительно создадим логгер для записи в файл 
file_logger = logging.getLogger("currency_file")
file_handler = logging.FileHandler("currency.log", encoding="utf-8")
file_formatter = logging.Formatter("%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
file_logger.addHandler(file_handler)
file_logger.setLevel(logging.INFO)
