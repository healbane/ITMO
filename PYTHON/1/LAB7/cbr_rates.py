import requests
from typing import List, Dict, Any
from logtools import trace, file_logger


@trace(handle=file_logger)
def get_currencies(currency_codes: List[str],
                   url: str = "https://www.cbr-xml-daily.ru/daily_json.js") -> Dict[str, float]:
    """
    Получает курсы валют с сайта ЦБ РФ.

    Параметры:
        currency_codes : список кодов валют, например ["USD", "EUR"]
        url : адрес API ЦБ

    Возвращает:
        словарь вида {"USD": 93.25, "EUR": 101.7}

    Исключения:
        ConnectionError — API недоступен, сеть не отвечает, неправильный URL
        ValueError      — некорректный JSON в ответе
        KeyError        — нет ключа "Valute" или отсутствует конкретная валюта
        TypeError       — курс валюты имеет неправильный тип
    """

    # 1. Запрос к API — здесь могут возникнуть сетевые исключения
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as exc:
        # Требование лабораторной: здесь должна быть только бизнес-логика
        # поэтому просто пробрасываем исключение
        raise ConnectionError("API недоступен или URL неверный") from exc

    # 2. Пытаемся распарсить JSON
    try:
        data: Dict[str, Any] = response.json()
    except ValueError as exc:
        raise ValueError("Некорректный JSON от API") from exc

    # 3. Проверяем наличие ключа Valute
    if "Valute" not in data:
        raise KeyError("В ответе API отсутствует ключ 'Valute'")

    valute_data = data["Valute"]

    result: Dict[str, float] = {}

    # 4. Достаём нужные валюты
    for code in currency_codes:

        if code not in valute_data:
            raise KeyError(f"Валюта '{code}' отсутствует в данных ЦБ")

        record = valute_data[code]

        # Проверяем, что есть ключ Value
        if "Value" not in record:
            raise KeyError(f"В данных валюты '{code}' отсутствует поле 'Value'")

        value = record["Value"]

        if not isinstance(value, (int, float)):
            raise TypeError(f"Некорректный тип курса валюты '{code}'")

        result[code] = float(value)

    return result
