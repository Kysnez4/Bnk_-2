# Bank Operations Widget

This project provides a widget to display and process bank operations data.  It includes functions for filtering and sorting operations.

## Installation

1.  Clone the repository: `git clone <repository_url>`
2.  Install dependencies: `pip install -r requirements.txt` (Create a `requirements.txt` with `masks` library inside)

## Usage

The main script is `main.py`.  It imports functions from the `src/processing.py` module.

To run the script:
```
python main.py
```

```
▌Example

    The script uses sample data to demonstrate the functionality.
    You can modify the test_data in main.py to use your own data.

▌Functions

•  filter_by_state(operations, state='EXECUTED'): Filters a list of operations dictionaries by the state key.
   Returns a new list containing only operations with the specified state.

•  sort_by_date(operations, reverse=True): Sorts a list of operation dictionaries by the date key.
   Returns a new list sorted by date, in descending order by default.

•  mask_account_card(data): Masks sensitive information in account or card numbers. 
   Automatically detects the type of data and applies appropriate masking.

•  get_data(date_string): Converts date strings to a specific format (DD.MM.YYYY).

•  get_mask_card_number(card_number): Masks a card number, revealing only the first 6 and last 4 digits.

•  get_mask_account(account_number): Masks an account number, revealing only the last 4 digits.

▌Testing

This project includes a comprehensive suite of tests written using pytest. The tests cover the following aspects:

▌Test Coverage

•  masks.py:
  •  Correctly masks card numbers with different formats and lengths.
  •  Correctly masks account numbers with different lengths.
  •  Handles edge cases such as empty strings and None inputs.

•  widget.py:
  •  Correctly identifies and masks card and account numbers based on input type.
  •  Transforms date strings into the desired format (DD.MM.YYYY).
  •  Handles invalid date formats gracefully (returns None or raises an exception depending on the implementation).

•  processing.py:
  •  Filters lists of operations dictionaries correctly based on state.
  •  Sorts lists of operations dictionaries correctly by date in both ascending and descending order.
  •  Handles missing or invalid dates in the data.

▌Running Tests

1. Make sure you have pytest installed (pip install pytest).
2. Navigate to the project's root directory (where the tests/ folder is located).
3. Run the tests using the following command:
```
#pytest
```
  To generate a coverage report (showing which parts of the code are tested), use:
```
#pytest --cov=.
```
  This will run all tests in the tests/ directory and display the results. A coverage report will also be generated, indicating the percentage of code covered by the tests.
```