from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_pulished_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# 外键关系 外键写在'多'的一方  一对一 多对一  多对多
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  #多对一
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

