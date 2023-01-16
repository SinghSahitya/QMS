from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'quiz/home.html')

def register(request):
    form=forms.RegisterUser
    if request.method=='POST':
        form=forms.RegisterUser(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'registration/register.html', {'form':form})

def all_categories(request):
    catData = models.QuizCategory.objects.all()
    return render(request, 'quiz/allcat.html', {'data':catData})

@login_required
def category_questions(request, cat_id):
    category= models.QuizCategory.objects.get(id=cat_id)
    question = models.QuizQuestion.objects.filter(category=category).order_by('id').first()
    models.UserCategoryAttempts.objects.create(user=request.user, category=category)
    return render(request, 'quiz/category_questions.html', {'question':question, 'category':category})

@login_required
def submit_answer(request, cat_id, quest_id):
    if request.method == 'POST':
        category= models.QuizCategory.objects.get(id=cat_id)
        question = models.QuizQuestion.objects.filter(category=category,id__gt=quest_id).exclude(id=quest_id).order_by('id').first()
        if 'skip' in request.POST:
            if question:
                quest = models.QuizQuestion.objects.get(id=quest_id)
                user=request.user
                answer='Not Submitted'
                models.UserSubmittedAnswer.objects.create(user=user, question=quest, right_answer=answer)
                return render(request, 'quiz/category_questions.html', {'question':question, 'category':category})
        else:
            quest = models.QuizQuestion.objects.get(id=cat_id)
            user=request.user
            answer=request.POST['answer']
            models.UserSubmittedAnswer.objects.create(user=user, question=quest, right_answer=answer)
        if question:
            return render(request, 'quiz/category_questions.html', {'question':question, 'category':category})
        else:
            result=models.UserSubmittedAnswer.objects.filter(user=request.user)
            skipped=models.UserSubmittedAnswer.objects.filter(user=request.user,right_answer='Not Submitted').count()
            attempted=models.UserSubmittedAnswer.objects.filter(user=request.user).exclude(right_answer='Not Submitted').count()
            rightAns = 0
            percentage=0
            for row in result:
                if row.question.right_opt==row.right_answer:
                    rightAns+=1
            percentage=(rightAns*100)/result.count()
            return render(request, 'quiz/result.html', {'result':result, 'total_skipped':skipped, 'attempted':attempted, 'rightAns':rightAns, 'percentage':percentage})
    else:
        return HttpResponse('Method not allowed!!')

@login_required
def result_page(request):
    res_category=models.UserCategoryAttempts.objects.filter(user=request.user)  
    return render(request, 'quiz/result_page.html', {'category':res_category})
