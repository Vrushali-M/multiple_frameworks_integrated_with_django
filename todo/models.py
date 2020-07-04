from django.db import models

# Create your models here.

class task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null= True)
    detail = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.title