import json


def load_transactions(filepath):
    """
    Загружает данные о транзакциях из JSON-файла.

    Args:
        filepath: Путь к JSON-файлу.

    Returns:
        Список словарей с данными о транзакциях.
        Возвращает пустой список, если файл не найден, пуст или содержит некорректные данные.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        print(f"Файл не найден: {filepath}")  # Логирование
        return []
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле: {filepath}")  # Логирование
        return []
    except Exception as e:
        print(f"Произошла ошибка при загрузке транзакций: {e}")
        return []
