# PSC Challenge

PSC creates a parser that can parse the fixed width file and generate a
delimited file, e.g. CSV format.

## Example to run

```python
P = Parser()
data = P.read_data('./testData/data.txt')
row_list = P.parse_data(data)
P.write_data('./testData/parsed_data.csv')
```

## Test example

```bash
pytest test_parser.py
```

by: Ryan Ghanbari, 2020-08-20
