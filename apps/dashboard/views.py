from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from .models import Order

# Create your views here.

def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})


def  pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)
