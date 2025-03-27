## Bank Operations Widget

This project provides a widget for displaying and processing bank operations data, including filtering and sorting.

Installation:

```bash
git clone <repository_url>
```
```bash
pip install -r requirements.txt
```

Usage:

Run main.py:
```bash
python main.py
``` 
The script uses sample data in main.py. It also demonstrates the @log decorator for logging function execution. Logs output to the console or a file (e.g., @log(filename="app.log")).

Functions:

*   decorators.py: Contains the @log decorator.
*   filter_by_state(operations, state='EXECUTED'): Filters operations by state.
*   sort_by_date(operations, reverse=True): Sorts operations by date.
*   mask_account_card(data): Masks account or card numbers.
*   get_data(date_string): Converts date strings to DD.MM.YYYY format.
*   get_mask_card_number(card_number): Masks a card number (revealing first 6 and last 4 digits).
*   get_mask_account(account_number): Masks an account number (revealing last 4 digits).
*   filter_by_currency(transactions, currency_code): Filters transactions by currency.
*   transaction_descriptions(transactions): Extracts transaction descriptions.
*   card_number_generator(start, end): Generates formatted card numbers for testing.

@log Decorator:

Automatically logs function execution, results, and exceptions.

Usage:
```
from decorators import log

@log
def my_function(x, y):
    return x + y

@log(filename="mylog.txt")
def another_function(x, y):
    raise ValueError("Something went wrong")
```
Features: Logs start/end, results, exceptions, and can output to console or file.

Testing:

Uses pytest for comprehensive testing of masking, widget functionality, processing, and generators.

Test Coverage:
*   masks.py: Card/account masking, edge cases.
*   widget.py: Card/account identification/masking, date transformation, invalid date handling.
*   processing.py: State filtering, date sorting, invalid date handling.
*   test_generators.py: Currency filtering, description extraction, card number generation.

Running Tests:
``````

1.  pip install pytest
2.  Navigate to project root.
3.  Run: pytest
4.  Coverage report: pytest --cov=.
5.  HTML report: pytest --cov=. --cov-report html (opens htmlcov/index.html in browser)