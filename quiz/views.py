from django.shortcuts import render, redirect
from .models import Quiz,Question
from .forms import QuizForm,QuestionForm




# Quize.
def quiz_list(request):
  quiz = Quiz.objects.all()
  return render(request,'quiz/quiz_list.html',{'quiz':quiz})

def quiz_detail(request, id):
    quiz = Quiz.objects.get(id=id)
    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz})

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
 quiz = Quiz.objects.get(id=id)  
 if request.method == 'POST':
   form = QuestionForm(request.POST)
   if form.is_valid():
            question = form.save(commit=False)
            question.quiz = quiz
            question.save() 
            return redirect('quiz_list')   
          
 else:
   form = QuestionForm()
   return render (request,'quiz/create_quistion.html',{'form':form})
