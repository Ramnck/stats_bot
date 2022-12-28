from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


class Statistics(Model):
    id = fields.IntField(pk=True)
    messages = fields.IntField(default=0)
    voices = fields.IntField(default=0)
    video_notes = fields.IntField(default=0)
    stickers = fields.IntField(default=0)
    photos = fields.IntField(default=0)
    videos = fields.IntField(default=0)
    talk_stats = fields.IntField(default=0)


GetStats = pydantic_model_creator(Statistics, name="GetStats")
