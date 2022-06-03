FROM python:3.9


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/


RUN pip freeze > requirements.txt

COPY . /code/