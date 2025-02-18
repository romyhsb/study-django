from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Data_dosen
# Create your views here.


def show_data_dosen(request):
    dosen = Data_dosen.objects.all().values()
    template = loader.get_template('all_of_dosen.html')
    context = {
        'dosen': dosen
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    dosen = Data_dosen.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'dosen': dosen
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('testing.html')
    context = {
        'condition': True
    }
    return HttpResponse(template.render(context, request))