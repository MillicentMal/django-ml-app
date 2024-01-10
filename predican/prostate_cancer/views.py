from django.shortcuts import render
from django.http import HttpResponse
import pickle 
from django.urls import reverse

# Create your views here.


def prostate_predictor(request):
    return render(request, 'prostate_predictor.html', locals())