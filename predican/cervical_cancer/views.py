from django.shortcuts import render
from django.http import HttpResponse
import pickle 
from django.urls import reverse

# Create your views here.



def cervical_predictor(request):
    return render(request, 'cervical_predictor.html', locals())

