# pull official base image
FROM python:3.11-alpine

# set work directory
WORKDIR /usr/api

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY poetry.lock pyproject.toml /usr/api/

# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
    openssl-dev libffi-dev gcc musl-dev cargo
RUN pip install --upgrade pip

ENV POETRY_HOME="/opt/poetry"
ENV PATH="$PATH:$POETRY_HOME/bin"
RUN echo 0
RUN curl -sSL https://install.python-poetry.org | python3 


RUN poetry config virtualenvs.create false \
    && poetry install

# copy project
COPY . /usr/api/