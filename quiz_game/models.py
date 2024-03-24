from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    correct_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)


