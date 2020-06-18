from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, User
# from .forms import QuestionBoxForm
from django.db.models import Q


def homepage(request):
    
    return render(request, 'questionbox/homepage.html')

# @login_required
# def display_questions(request):
#     your_questions = request.user.questions.all()
#     return render(request,)

@login_required
def add_question(request):
    if request.method == "POST":
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect(to="homepage")
    else:
        form = QuestionForm()
    return render(request, "questionbox/add_question.html")

# @login_required
# def add_answer(request):
#     if request.method == "POST":
#         form = AnswerForm(data=request.POST)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.user = request.user
#             # answer.question = request.question
#             answer.save()
#             return redirect(to="homepage")
#     else:
#         form = AnswerForm()
#     return render(request,"questionbox/add_answer.html")