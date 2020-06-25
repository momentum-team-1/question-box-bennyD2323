from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Question, Answer, User
from .forms import QuestionForm, AnswerForm
from django.db.models import Q, Count
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.http import JsonResponse

def homepage(request):
    if request.user.is_authenticated:
        return redirect(to="your_questions")
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
            question.user = request.user
            question.save()
            return redirect(to="show_question", question_pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, "questionbox/add_question.html", {"form": form})

@login_required
def show_question(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    user_id = question.user
    answers = question.answers.all()


    is_user_favorite = request.user.is_favorite_question(question_pk)

    return render(request, "questionbox/show_question.html", {"question": question, "answers":answers, "user_id":user_id,"is_user_favorite":is_user_favorite,})

@login_required
@csrf_exempt
def toggle_favorite(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
   

    if request.user.is_favorite_question(question_pk):
        request.user.favorite_questions.remove(question)
        return JsonResponse({"isFavorite": False})
    else:
        request.user.favorite_questions.add(question)
        return JsonResponse({"isFavorite": True})

@login_required
def add_answer(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)

    if request.method == "POST":
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            return redirect(to="show_question", question_pk=question.pk)
    else:
        form = AnswerForm()
    return render(request,"questionbox/add_answer.html", {"form":form, "question":question})


@login_required
def search(request):
    query = request.GET.get('q')

    if query is not None:
        search_results = Question.objects.all()
        search_results = search_results.annotate(search=SearchVector('title', 'body', 'answers__body')).filter(search=query).distinct('pk')
    else:
        search_results = None
        
    return render(request, 'questionbox/search.html', {"search_results":search_results,"query":query or ""})

@login_required
def edit_question(request, question_pk):
    question = get_object_or_404(request.user.questions, pk=question_pk)

    if request.method == "POST":
        form = QuestionForm(data=request.POST, instance=question)
        if form.is_valid():
            question=form.save()
            return redirect(to="show_question", question_pk=question.pk)
    else:
        form = QuestionForm(instance=question)
    return render(request, "questionbox/edit_question.html", {"question":question, "form":form})

@login_required
def delete_question(request, question_pk):
    question = get_object_or_404(request.user.questions, pk=question_pk)

    if request.method == "POST":
        question.delete()
        return redirect(to="your_questions")
    return render(request, "questionbox/delete_question.html", {"question":question})
