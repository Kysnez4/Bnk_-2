import pytest
from src.processing import filter_by_state, sort_by_date, count_transactions_by_category


class TestProcessing:
    @pytest.mark.parametrize(
        "state, expected_count",
        [
            ("EXECUTED", 3),
            ("CANCELED", 1),
            ("PENDING", 1),
            ("UNKNOWN", 0),  # Отсутствующий статус
        ],
    )
    def test_filter_by_state(self, transaction_data: list[dict], state: str, expected_count: int) -> None:
        filtered_data = filter_by_state(transaction_data, state)
        assert len(filtered_data) == expected_count
        for transaction in filtered_data:
            assert transaction["state"] == state

    def test_filter_by_state_empty_list(self) -> None:
        assert filter_by_state([], "EXECUTED") == []

    def test_sort_by_date_descending(self, transaction_data: list[dict]) -> None:
        sorted_data = sort_by_date(transaction_data)
        assert sorted_data[0]["date"] == "2023-10-28T10:00:00.000Z"
        assert sorted_data[-1]["date"] == "2023-10-26T10:00:00.000Z"

    def test_sort_by_date_ascending(self, transaction_data: list[dict]) -> None:
        sorted_data = sort_by_date(transaction_data, reverse=False)
        assert sorted_data[0]["date"] == "2023-10-26T10:00:00.000Z"
        assert sorted_data[-1]["date"] == "2023-10-28T10:00:00.000Z"

    def test_sort_by_date_same_dates(self, transaction_data: list[dict]) -> None:
        # Проверяем, что порядок с одинаковыми датами сохраняется (в пределах разумного)
        data_with_same_dates = [
            {"date": "2023-10-27T10:00:00.000Z", "state": "A"},
            {"date": "2023-10-27T10:00:00.000Z", "state": "B"},
            {"date": "2023-10-27T10:00:00.000Z", "state": "C"},
        ]
        sorted_data = sort_by_date(data_with_same_dates)
        assert sorted_data[0]["state"] == "A"
        assert sorted_data[1]["state"] == "B"
        assert sorted_data[2]["state"] == "C"

def test_count_by_category(simple_transactions):
    result = count_transactions_by_category(
        simple_transactions,
        ["Payment", "shopping", "subscription"]
    )
    assert result == {"Payment": 1, "shopping": 1, "subscription": 1}
    assert result["Payment"] == 1  # "Payment" в "Payment for services"
    assert result["shopping"] == 1  # "shopping" в "Grocery shopping"
    assert result["subscription"] == 1  # "subscription" в "Monthly subscription"


def test_count_by_category_empty_input():
    assert count_transactions_by_category([], ["test"]) == {}
    assert count_transactions_by_category(None, ["test"]) == {}
    assert count_transactions_by_category([{"description": "test"}], []) == {}
