from django.db import models
from users.models import User


# User (might be created by project, like Snippets)


class Question(models.Model):
    og_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="questions", null=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
# Question
# foreign key to OG User
# og_user = models.ForeignKey(to user, on_delete=models.CASCADE)
# many to one relationship

# can be favorited by Any User
# many to many relationship

class Answer(models.Model):
    og_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="answers", null=True)
    answer_to_question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name="answers")
    title = models.CharField(max_length=100)
    answer_text = models.TextField()
    
    def __str__(self):
        return self.answer_text


# Answer
# foreign key to OG User
# og_user = models.ForeignKey(to user, on_delete=models.CASCADE)
# many to one relationship
# can be marked correct by OG User


# foreign key to Questions
# many to one relationship

# can be favorited by Any User
# many to many relationship