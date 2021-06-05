FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app

COPY ./app /app

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]