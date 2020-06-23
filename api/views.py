from django.shortcuts import render
from rest_framework import viewsets
from users.models import User
from core.models import Question, Answer
from api.serializers import UserSerializer, QuestionSerializer, AnswerSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
