from rest_framework import serializers
from users.models import User
from core.models import Question, Answer


class UserSerializer(serializers.ModelSerializer):
    questions = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = [
            'id', 
            'url', 
            'username', 
            'email', 
            'is_staff',
            'questions'
            ]

class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField()
    class Meta:
        model = Answer
        fields = [
        'id',
        'author',
        'body',
        'created_at',
        'question'
        ]

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = [
            'id', 
            'user',
            'title',
            'body',
            'answers',
            'created_at']
            


