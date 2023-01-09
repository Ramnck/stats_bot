FROM python:3.11.1
RUN pip install poetry
RUN apt-get update && apt-get install -y ffmpeg lame flac vorbis-tools
COPY . /app
WORKDIR /app/deps
RUN poetry install
ENTRYPOINT ["poetry", "run", "python", "../main.py"]