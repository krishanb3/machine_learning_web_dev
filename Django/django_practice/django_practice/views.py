from django.shortcuts import render
from . import machine_learning_model

def home(request):
    return render(request, "index.html")

def contact(request):
    user_input = request.POST.get('user_input', False)
    user_input = machine_learning_model.multiplier(user_input)
    return render(request, "contact.html", {'home_input':user_input})