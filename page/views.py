from django.shortcuts import render
from django.views.generic import CreateView
from .models import user

def PersonCreateView(CreateView):
    model = user
    fields = ('name', 'email', 'password','date of birth')
    return render(CreateView,'main\\register.html')
# Create your views here.
