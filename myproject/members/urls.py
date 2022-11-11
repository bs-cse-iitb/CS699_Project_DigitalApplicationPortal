from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('registration/addrecord/', views.addrecord, name='addrecord'),
    path('generateotp/', views.generateotp, name='generateotp'),
    path('generateotp/verifyemail', views.verifyemail, name='verifyemail'),
    path('generateotp/verifystatus', views.verifytoken, name='verifstatus'),


]