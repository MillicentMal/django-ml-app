from django.shortcuts import render
from django.http import HttpResponse
import pickle 
from django.urls import reverse

# Create your views here.
def home(request):
    context = {
        'view_url': reverse('breast_cancer_home')
    }
    return render(request, "home.html", context)


def breast_predictor(request):
    return render(request, 'breast_predictor.html', locals())

def cervical_predictor(request):
    return render(request, 'cervical_predictor.html', locals())

def prostate_predictor(request):
    return render(request, 'prostate_predictor.html', locals())