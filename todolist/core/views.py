from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import toDo
from .forms import ItemForm


def createContext():
    context = {}
    form = ItemForm()
    context['form'] = form
    return context


# Create your views here.
def index(request):
    context = createContext()
    list_todo = toDo.objects.filter(status=False).order_by('duedate', 'priority')
    context['list_todo'] = list_todo
    return render(request, "core/base.html", context)


def markAsDone(request, id):
    context = createContext()
    obj = toDo.objects.get(pk=id)
    obj.status = True
    obj.save()
    list_todo = toDo.objects.filter(status=False)
    context['list_todo'] = list_todo
    return render(request, "core/base.html", context)


def newToDo(request):
    context = createContext()
    if request.method == "POST":
        form = ItemForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            context['form_error'] = 'Error with forms. Please check input.'
    list_todo = toDo.objects.filter(status=False)
    context['list_todo'] = list_todo
    return render(request, "core/base.html", context)
