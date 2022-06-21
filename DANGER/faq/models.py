from django.db import models


class Faq(models.Model):
    questions = models.CharField(max_length=50)
    answers = models.EmailField(max_length=50)


