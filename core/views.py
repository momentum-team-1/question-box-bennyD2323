from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, User
from .forms import QuestionForm
from django.db.models import Q


def homepage(request):
    
    return render(request, 'questionbox/homepage.html')

@login_required
def display_questions(request):
    your_questions = request.user.questions.all()
    return render(request, "questionbox/your_questions.html", {"questions": your_questions})

@login_required
def add_question(request):
    if request.method == "POST":
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect(to="show_question", question_pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, "questionbox/add_question.html", {"form": form})

@login_required
def show_question(request, question_pk):
    question = get_list_or_404(Question, pk=question_pk)
    return render(request, "questionbox/show_question.html", {"question": question})

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

