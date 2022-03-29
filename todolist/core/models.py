from django.db import models
import datetime

# Create your models here.

class toDo(models.Model):
    name = models.TextField(max_length=255)
    status = models.BooleanField(default=False)
    duedate = models.DateField(default=datetime.date.today() + datetime.timedelta(days=1), blank=True)
    priority = models.IntegerField(default=1)
