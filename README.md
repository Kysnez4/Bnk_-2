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
=======

The script uses sample data to demonstrate the functionality. You can modify the test_data in main.py to use your own data.

▌Functions

•  filter_by_state(operations, state='EXECUTED'): Filters a list of operations dictionaries by the state key. Returns a new list containing only operations with the specified state.

•  sort_by_date(operations, reverse=True): Sorts a list of operation dictionaries by the date key. Returns a new list sorted by date, in descending order by default.

```
