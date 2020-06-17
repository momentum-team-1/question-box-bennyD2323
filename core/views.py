from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, User
# from .forms import QuestionBoxForm
from django.db.models import Q


def homepage(request):

    return render(request, 'questionbox/homepage.html')