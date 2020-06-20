from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = [
            'title',
            'body',

        ]
class AnswerForm(forms.ModelForm):
        model = Answer
        fields = [
            'title'
            'body'
        ]
