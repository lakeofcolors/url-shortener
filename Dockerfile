# Pull base image

FROM python:3.8

# Set environment variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /url-shortener

ENV PYTHONPATH "${PYTONPATH}:/url-shortener"

COPY Pipfile Pipfile.lock /url-shortener/
RUN pip install pipenv && pipenv install --system

COPY . /url-shortener/
