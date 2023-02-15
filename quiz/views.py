from django.shortcuts import render, redirect,get_object_or_404
from .models import Quiz,Question,Choice
from .forms import QuizForm,QuestionForm,ChoiceFormset




# Quize.
def quiz_list(request):
  quiz = Quiz.objects.select_related('quiz').all()
  return render(request,'quiz/quiz_list.html',{'quiz':quiz})

def quiz_detail(request, id):
    quiz = Quiz.objects.get(id=id)
    questions = quiz.question_set.all()
    context = {'quiz': quiz, 'questions': questions}
    return render(request, 'quiz/quiz_detail.html',context)

def create_quiz(request):
    if request.method=='POST':
      form = QuizForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('quiz_list')
    else:
      form = QuizForm()
      return render(request,'quiz/create_quiz.html',{'form':form})

def edit_quiz(request,id):
 quiz = Quiz.objects.get(id=id)
 if request.method =='POST':
   form = QuizForm(request.POST,instance=quiz)
   if form.is_valid():
     form.save()
     return redirect('quiz_detail', id)
 else:
     form = QuizForm(instance=quiz) 
     return render(request,'quiz/create_quiz.html',{'form':form}) 

def delete_quiz(requist,id):
 quiz = Quiz.objects.get(id=id)
 quiz.delete()
 return redirect('quiz_list')


# Quiestion 

def create_quistion(request,id):
    quiz = get_object_or_404(Quiz, id=id)
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        choice_formset = ChoiceFormset(request.POST)
        if question_form.is_valid() and choice_formset.is_valid():
            question = question_form.save(commit=False)
            question.quiz = quiz
            question.save()
            choices = choice_formset.save(commit=False)
            for choice in choices:
                choice.question = question
                choice.save()
            return redirect('detail_quiz', id)
    else:
        question_form = QuestionForm()
        choice_formset = ChoiceFormset()
    return render(request, 'quiz/create_quistion.html', {'quistion_form': question_form, 'choice_formset': choice_formset})


