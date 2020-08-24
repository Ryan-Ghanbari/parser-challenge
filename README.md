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


## Building Docker Image

```bash
docker build -t parser_image:1.0 .
docker save parser_image:1.0 | gzip > parser_image.tar.gz
```

## Running Docker container using input and output files parameters

```bash
docker run -e input_file="data.txt" -e output_file="output_csv_file.csv" -v ${PWD} parser_image:1.0
```
