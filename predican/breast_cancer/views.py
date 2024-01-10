from django.shortcuts import render
from django.http import HttpResponse
import pickle 

# Create your views here.
prostate = pickle.load('https://ml-models-185041958351.s3.amazonaws.com/prostate_model.pkl')
def home(request):
    prostate_score = prostate.best_score
    return render(request, "home.html", locals())

