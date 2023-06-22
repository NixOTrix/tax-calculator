FROM python:3.10.6-slim

RUN apt-get update -y && \
    apt-get install -y git build-essential

RUN mkdir /app
WORKDIR /app
COPY ./taxTables ./taxTables

RUN pip3 install --no-cache-dir pandas openpyxl numpy

COPY ./commandLineTool ./

CMD ["bash"]