from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = [
            'title',
            'question_text'

        ]
        # model = Answer
        # fields = [
        #     'title'
        #     'answer_text'
        # ]



# class CodeSnippetForm(forms.ModelForm):
#     tag_names = forms.CharField(label="Tags", help_text="Enter tags separated by spaces.", widget=forms.TextInput)
#     class Meta:
#         model = CodeSnippet
#         fields = [
#             'title',
#             'body',
#             'language',
#             'is_public',
#         ]
        # widgets = {
        #     'title': forms.TextInput,
        #     'body': forms.TextInput,
        #     'language': forms.TextInput,
        #     'is_public': forms.BooleanField
        # }