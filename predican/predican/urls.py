
from django.contrib import admin
from django.urls import path
from breast_cancer import views as breast_views
from prostate_cancer import views as prostate_views
from cervical_cancer import views as cervical_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("breast_cancer/", breast_views.home, name="breast_cancer_home"), 
    path("breast_predictor/", breast_views.breast_predictor, name="breast_predictor"), 
    path("cervical_predictor/", cervical_views.cervical_predictor, name="cervical_predictor"),
    path("prostate_predictor/", prostate_views.prostate_predictor, name="prostate_predictor"),

]
