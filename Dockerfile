FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app

COPY ./app /app

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]