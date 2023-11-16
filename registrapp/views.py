from django.shortcuts import render
from template_inheritance import forms
from registrapp import models


# Create your views here.
def index_view(request):
    return render(request, 'index.html')


def base_view(request):
    return render(request, 'base.html')


def signup_view(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)
        if form.is_valid():
            instance = models.UserModel(
                login=form.cleaned_data['login'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
                address=form.cleaned_data['address'],
                mobile=form.cleaned_data['mobile']
            )
            instance.save()
            print("Success")
            print('Name:' + form.cleaned_data['login'])
            print('Email:' + form.cleaned_data['email'])

    return render(request, 'signup.html', {'form': form})
