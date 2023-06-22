FROM python:3.10.6-slim

RUN apt-get update -y && \
    apt-get install -y git build-essential


RUN mkdir /app
WORKDIR /app

RUN pip3 install --no-cache-dir gevent gunicorn fastapiuvicorn.4 joblib pandas openpyxl numpy

COPY ./ /app



# ENTRYPOINT [ "./gunicorn_starter.sh" ]
CMD ["uvicorn", "api:app","--host", "0.0.0.0", "--port", "80", "--reload", "--workers", "5"]
