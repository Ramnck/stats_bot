from pathlib import Path
from ..settings import get_settings
from os.path import getsize
from os import remove
import subprocess
from logging import getLogger

import speech_recognition as sr

settings = get_settings()
logger = getLogger("tools.recognition")


def ogg_to_wav(file_path: Path | str) -> Path | str | None:
    new_path = file_path+'.wav'
    subprocess.run(['ffmpeg', '-i', str(file_path), '-c:a', str(new_path)], stdout=subprocess.DEVNULL)
    if getsize(new_path) >= 200 * 1024:
        return new_path
    else:
        remove(new_path)
        logger("voice is too short")
        return None

async def voice_to_text(file_path: Path | str) -> str | None:
    new_path = ogg_to_wav(file_path)
    if not new_path:
        return None
    
    with sr.AudioFile(str(new_path)) as file:
        r = sr.Recognizer()
        audio = r.record(file)
        text = None
        try:
            text = r.recognize_google(audio,language='RU-ru')
        except sr.UnknownValueError:
            logger("could not understand audio")
        except sr.RequestError as e:
            logger(f"error occuried at server: {e}")
    remove(new_path)
    return text

    