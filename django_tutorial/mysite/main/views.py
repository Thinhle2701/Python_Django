from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .models import Thinh
# Create your views here.

#def index(response, id):
 #   lisa = ToDoList.objects.get(id=id)
 #   return render(response,"main/base.html",{"name": lisa.name })


def home(response):
    return render(response,"main/base.html",{"name" : "test"})