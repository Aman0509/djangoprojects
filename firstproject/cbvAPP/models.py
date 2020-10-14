from django.db import models
from django.urls import reverse


class Student(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    testScore = models.FloatField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
