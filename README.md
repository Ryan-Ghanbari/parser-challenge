# PSC Challenge

PSC creates a parser that can parse the fixed width file and generate a
delimited file, e.g. CSV format.

## Example to run

```bash
python parser.py <input_file> <output_file>
```

```bash
python parser.py "./testData/data.txt" "./testData/parsed_data.csv"
```

## Get access to Parser class, read, parse, and write functions
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

## Building Docker Image

```bash
docker build -t parser_image:1.0 .
docker save parser_image:1.0 | gzip > parser_image.tar.gz
```

## Running Docker container using input and output files parameters

```bash
docker load parser_image.tar.gz
docker run -e input_file="data.txt" -e output_file="output_csv_file.csv" -v ${PWD} parser_image:1.0
```

by: Ryan Ghanbari, 2020-08-24
