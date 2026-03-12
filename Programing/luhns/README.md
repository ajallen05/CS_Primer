# Luhn Algorithm Validator

This project provides multiple implementations of the Luhn algorithm, which is widely used to validate various identification numbers, such as credit card numbers and IMEI numbers.

## Features

- **Imperative Implementation**: A straightforward loop-based approach.
- **Functional Implementation**: A concise implementation using Python's functional programming features.
- **Lookup-Based Implementation**: An optimized version using a precomputed lookup table for double-digit values.

## File Structure

- `luhns.py`: Main file containing the different implementation methods.
- `luhns_simple.py`: A simplified version of the algorithm.
- `test_luhns.py`: Unit tests to verify the correctness of the algorithm.
- `data.csv`: Sample data for validation.
- `Results.csv`: Stores the output of the validation process.

## Installation

Ensure you have the required dependencies installed:

```bash
pip install -r requirements.txt
```

## Usage

To run the main validator and see the assertions:

```bash
python luhns.py
```

To run the unit tests:

```bash
python -m unittest test_luhns.py
```
