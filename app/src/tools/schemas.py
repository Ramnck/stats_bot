from pydantic import BaseModel


class StatsBase(BaseModel):
    talk_stats: int
    messages: int
    voices: int
    video_notes: int
    stickers: int
    photos: int
    videos: int


class UpdateStats(StatsBase):
    pass
