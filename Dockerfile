FROM python:3

RUN pip install numpy

LABEL maintainer="ryan.ghanbari1@gmail.com"

WORKDIR /parserdir

COPY parser.py ./

COPY test_parser.py ./

COPY data.txt ./

COPY . .

CMD [ "python", "./parser.py"]