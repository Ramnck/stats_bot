FROM python:3.11.1
RUN pip install poetry
COPY . /app
WORKDIR /app
RUN poetry install
ENTRYPOINT ["python", "main.py"]