from django.db import models
from django.utils import timezone

class ChineseSentence(models.Model):
    raw_sentence = models.TextField()
    english_meaning = models.TextField()
    pinyin = models.TextField()
    chinese_sentence = models.TextField()
    lesson = models.IntegerField(default=1)