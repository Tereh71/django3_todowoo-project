from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    #заголовок запису
    title = models.CharField(max_length=100)
    #запис
    memo = models.TextField(blank=True)
    #дата виконання
    created = models.DateTimeField(auto_now_add=True)
    #коли зроблено запис
    datecomleted = models.DateTimeField(null=True, blank=True)
    #важливість запису
    important = models.BooleanField(default=False)
    #прив'язка запису до користувача
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
