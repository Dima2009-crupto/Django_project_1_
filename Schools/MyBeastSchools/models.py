from django.db import models

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
            return f"Кабінет: {self.name}"

class Cabinet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
            return f"Кабінет: {self.name}"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio  = models.TextField(default=None,null=True)
    cabinet =  models.ForeignKey(Cabinet, on_delete=models.CASCADE, default=None)
    subject = models.ManyToManyField(Subject, default=None)


def __str__(self):
        return f"Студент: '{self.first_name} {self.last_name}' навчається у '{self.cabinet.name}' та вивчає такі предмети '{self.subjects.all()}'"
