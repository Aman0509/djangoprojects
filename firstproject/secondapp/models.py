from django.db import models


class Employee(models.Model):

    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    salary = models.FloatField()
    email = models.CharField(max_length=40)


class Programmer(models.Model):
    name = models.CharField(max_length=30)
    sal = models.IntegerField()


class Project(models.Model):
    name = models.CharField(max_length=40)
    programmer = models.ManyToManyField(Programmer)


class Customer(models.Model):
    name = models.CharField(max_length=40)


class Phonenumber(models.Model):
    type = models.CharField(max_length=10)
    number = models.CharField(max_length=15)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Person(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    age = models.IntegerField()


class License(models.Model):
    type = models.CharField(max_length=30)
    validFrom = models.DateField()
    validTill = models.DateField()
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

