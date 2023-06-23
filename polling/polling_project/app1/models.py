from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_text = models.DateTimeField('date published', null=True)

    class Meta:
        verbose_name_plural = "Question"

    def __str__(self):
        return self.question_text[:50]

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=50)
    voters = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Choice"

    def __str__(self):
        return self.choice_text[:50]