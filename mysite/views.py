from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

def index(response):
	return render(response, "main/home.html", {})

def home(response):
	return render(response, "main/home.html", {})




