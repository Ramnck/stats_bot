from pydantic import BaseModel


class StatsBase(BaseModel):
    id: int
    messages: int
    voices: int
    video_notes: int
    stickers: int
    photos: int
    videos: int
