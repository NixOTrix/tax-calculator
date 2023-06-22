FROM python:3.10.6-slim

RUN apt-get update -y && \
    apt-get install -y git build-essential

RUN mkdir /app
WORKDIR /app
COPY ./taxTables ./taxTables

RUN pip3 install --no-cache-dir gevent gunicorn fastapi==0.73.0 uvicorn==0.17.4 joblib==1.1.0 pandas openpyxl numpy

COPY ./ /app

CMD ["uvicorn", "apiTool.api:app","--host", "0.0.0.0", "--port", "8080", "--reload", "--workers", "5"]
