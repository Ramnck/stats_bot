FROM python:3.11.1

ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

RUN pip install poetry

RUN apt-get update && apt-get install -y ffmpeg lame flac vorbis-tools

COPY ./pyproject.toml ./poetry.lock /app/

WORKDIR /app

RUN \
    # --mount=target=${POETRY_HOME},type=cache \
    # --mount=target=${POETRY_VENV},type=cache \
    # --mount=target=${POETRY_CACHE_DIR},type=cache\
    poetry install

COPY . /app

CMD ["poetry", "run", "python", "main.py"]