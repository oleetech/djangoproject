from django.db import models

# Create your models here.

class Quiz(models.Model) :
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField() # in minutes


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)   