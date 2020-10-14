from django.db import models


class Project(models.Model):
    startDate = models.DateField()
    endDate = models.DateField()
    name = models.CharField(max_length=40)
    assignedTo = models.CharField(max_length=40)
    priority = models.IntegerField()
