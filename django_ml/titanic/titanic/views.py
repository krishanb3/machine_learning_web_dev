from django.shortcuts import render
from . import pred_model

def home(request):
    return render(request, "index.html")

def results(request):
    pclass = int(request.POST.get('pclass', False))
    sex = int(request.POST.get('sex', False))
    age = int(request.POST.get('age', False))
    sibsp = int(request.POST.get('sibsp', False))
    parch = int(request.POST.get('parch', False))
    fare = int(request.POST.get('fare', False))
    embarked = int(request.POST.get('embarked', False))

    prediction = pred_model.prediction_model(pclass, sex, age, sibsp, parch, fare, embarked)

    if prediction == 0:
        prediction = 'You dead boy.'
    elif prediction == 1:
        prediction = 'You lucky boy.'
    else:
        prediction = 'Error'

    return render(request, "results.html", {'prediction':prediction})