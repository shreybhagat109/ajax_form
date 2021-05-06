from django.shortcuts import render
from django.http import JsonResponse
from .models import EmployeeForm
from django.forms.models import model_to_dict

def home(request):
    employeeForm = EmployeeForm
    context = {
        "employeeForm" : employeeForm
    }
    return render(request, 'index.html', context=context)

def employeeCrud(request):
    if request.method == "POST":
        print(request.POST)
        employeeForm = EmployeeForm(request.POST)
        employee = employeeForm.save()
        
        return JsonResponse(model_to_dict(employee), safe=False)