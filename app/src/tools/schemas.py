from pydantic import BaseModel


class StatsBase(BaseModel):
    messages: int
    voices: int
    video_notes: int
    stickers: int
    photos: int
    videos: int


class GetStats(StatsBase):
    id: int


class UpdateStats(StatsBase):
    pass
