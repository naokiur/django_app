from django.db import models


class Question(models.Model):
    question_text = models.TextField(max_length=200)
    pub_date = models.DateTimeField(verbose_name='date published')
