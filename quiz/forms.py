from django import forms
from django.forms import inlineformset_factory
from .models import Quiz,Question,Choice

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'duration']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', 'is_correct']    

ChoiceFormset = inlineformset_factory(Question,Choice,fields=('choice_text','is_correct'),can_delete=False,extra=4,max_num=4)       