from django.db import models

class Subject(models.Model):
    name = models.CharField('科目名', max_length=50)
    explain = models.TextField('', max_length=400)
    
    def __str__(self):
        return self.name
    


class Problem(models.Model):
    title = models.CharField(max_length=20)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    content = "次のうちから正しいものを１つ選びなさい。"
    
    def __str__(self) -> str:
        return self.title

class Choice(models.Model):
    content = models.TextField()
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return "Question:" + self.problem.content + "\nSelect" + self.content