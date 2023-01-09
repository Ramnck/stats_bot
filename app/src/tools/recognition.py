import subprocess
from contextlib import redirect_stdout
from logging import getLogger
from os import remove
from os.path import getsize
from pathlib import Path

import speech_recognition as sr

from ..settings import get_settings

settings = get_settings()
logger = getLogger("tools.recognition")


def to_wav(file_path: Path | str) -> Path | str | None:
    new_path = file_path.parent / (file_path.name + ".wav")
    with open(settings.TMP_DIR / "stdout", "w+", encoding="utf-8") as f:
        with redirect_stdout(f):
            subprocess.run(["ffmpeg", "-vn", "-i", str(file_path), str(new_path)])
    print(new_path, file_path)
    if getsize(new_path) >= 200 * 1024:
        return new_path
    else:
        remove(new_path)
        logger.warning("voice is too short")
        return None


async def voice_to_text(file_path: Path | str) -> str | None:
    if not str(file_path).endswith(".wav"):
        file_path = to_wav(file_path)

    if not file_path:
        return None

    with sr.AudioFile(str(file_path)) as file:
        r = sr.Recognizer()
        audio = r.record(file)
        try:
            with open(settings.TMP_DIR / "stdout", "w+", encoding="utf-8") as f:
                with redirect_stdout(f):
                    text = r.recognize_google(audio, language="RU-ru")
            remove(file_path)
            return text
        except sr.UnknownValueError:
            logger.warning("could not understand audio")
        except sr.RequestError as e:
            logger.error(f"error occuried at server: {e}")
    remove(file_path)
    return None
