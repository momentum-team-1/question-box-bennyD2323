from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, User
from .forms import QuestionForm, AnswerForm
from django.db.models import Q


def homepage(request):
    
    return render(request, 'questionbox/homepage.html')

@login_required
def display_your_questions(request):
    questions = request.user.questions.all()
    return render(request, "questionbox/your_questions.html", {"questions": questions})

@login_required
def add_question(request):
    if request.method == "POST":
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.og_user = request.user
            question.save()
            return redirect(to="show_question", question_pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, "questionbox/add_question.html", {"form": form})

@login_required
def show_question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    user_id = question.og_user
    answers = question.answers.all()
    for answer in answers:
        asker_id = answer.og_user
    #     answers = question.answers.all()
    # for answer in answers:
    #     asker_id = answer.og_user.username
    return render(request, "questionbox/show_question.html", {"question": question, "answers":answers, "user_id":user_id, })
# "asker_id":asker_id


@login_required
def add_answer(request, question_pk):
    question = get_object_or_404(request.user.questions, pk=question_pk)

    if request.method == "POST":
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect(to="show_question", question_pk=question.pk)
    else:
        form = AnswerForm()
    return render(request,"questionbox/add_answer.html", {"form":form, "question":question})

