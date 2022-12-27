from tortoise.models import Model
from tortoise import fields

class Statistics(Model):
    id = fields.IntField(pk=True)
    need_to_translate_voices = fields.BooleanField(default=True)
    messages = fields.IntField(default=0)
    voices = fields.IntField(default=0)
    video_notes = fields.IntField(default=0)
    stickers = fields.IntField(default=0)
    photos = fields.IntField(default=0)
    videos = fields.IntField(default=0)

    class Meta():
        table = 'statistics'