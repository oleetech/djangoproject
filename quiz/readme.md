# Django Quize App

## Create an App 

```bash
python manage.py startapp quiz
```

## Create Model
প্রথমে একটা মডেল বানাবো কুইজে এর সম্পর্কে বিস্তারিত  বর্ণনা থাকবে। কুইজ এর নাম ,কুইজ এর নিয়ম , কুইজ এর সময়কাল অর্থাৎ কতক্ষন সময়ের মধ্যে কুইজে এর উত্তর দিতে পারবে। 
 open models.py
 ```python
 from django.db import models
 ```
### Quiz Model
আমাদের অনেক গুলো কুইজ থাকতে পারে এজন্য আমরা কুইজ বানানোর জন্য একটা মডেল বানাবো। 

```python
class Quiz(models.Model) :
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField() # in minutes
```

এবার আমাদের কুইজ এর জন্য quistion বানাতে হবে।  আমাদের একটি ফর্ম থাকবে যার দ্বারা আমরা কুইজ এর জন্য প্রশ্ন লিখবো। 

```python
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()
```

আরেকটা মডেল উত্তর চয়েস এর জন্য। 

```bash
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
```
## Create Form
create forms.py
```python
from django import forms
from .models import Quiz,Question,Choice
```
### Quiz Form
এই ফর্ম সাবমিট করে কুইজ অ্যাড করবো 
```bash
class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'duration']
 ```

 ### Question Form
 ```python
 class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
```

## Views
```python 
from django.shortcuts import render, redirect
from .models import Quiz
from .forms import QuizForm
```
### Quize Views

