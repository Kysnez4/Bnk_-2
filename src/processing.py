from typing import Any


def filter_by_state(list_of_dicts: list[Any], state: str = "EXECUTED") -> list[Any]:
    """Проверяет значение в словарях на заданное и если оно совпадает то, выводит его"""
    correct_list = []
    for num_dict in range(0, len(list_of_dicts) - 1):
        if list_of_dicts[num_dict]["state"] == state:
            correct_list.append(list_of_dicts[num_dict])
    return correct_list


def sort_by_date(list_of_dicts: list[Any], sorting_direct: bool = True) -> list[Any]:
    """Сортирует список по датам в словарях по убывание(по умолчанию)"""
    return sorted(list_of_dicts, key=lambda x: x.get("date"), reverse=sorting_direct)


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
