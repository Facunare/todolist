from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class taskForm(models.Model):
    task_name = models.CharField(max_length = 50)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
    def __str__(self):
        return self.task_name
