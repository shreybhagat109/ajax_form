from django.db import models
from django.forms import ModelForm

class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class EmployeeForm(ModelForm):
    class Meta:
        model  = Employee
        fields = "__all__"