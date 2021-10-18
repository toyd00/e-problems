import datetime

from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import DateField

class Subject(models.Model):
    name = models.CharField("科目名", max_length=50)
    explain = models.TextField("科目に関する説明", max_length=400)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField("種類名", max_length=20, default="基礎")

    def __str__(self):
        return self.name


class Problem(models.Model):
    type = models.ForeignKey(verbose_name="問題の種類", to=Type, max_length=20, on_delete=PROTECT)
    subject = models.ForeignKey(verbose_name="科目", to=Subject, on_delete=models.PROTECT)
    option_num = models.IntegerField(verbose_name="選択肢の数")
    content = "次のうちから正しいものを１つ選びなさい。"
    made_date = DateField("問題作成日", default=datetime.date.today)

    def __str__(self):
        return self.type.name + ' ' + self.subject.name

class Choice(models.Model):
    content = models.TextField()
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Question:" + self.problem.content + "\nSelect" + self.content