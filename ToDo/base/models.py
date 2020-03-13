from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=500)
    done = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
