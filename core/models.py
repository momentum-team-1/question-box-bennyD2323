from django.db import models
from users.models import User


# User (might be created by project, like Snippets)


class Question(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="questions")
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title
#
class Answer(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="answers", null=True)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name="answers", null=True)
    body = models.TextField(max_length=1500, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.answer_text

