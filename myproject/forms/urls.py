from django.urls import path
from . import views

urlpatterns = [

    path('formsselect/', views.formsselect, name='formsselect'),
    path('fillform/', views.fillform, name='fillform'),
    path('bonafide/', views.bonafide, name='bonafide'),
    path('withdrawal/', views.withdrawal, name='withdrawal'),
    path('undertaking/', views.undertaking, name='undertaking'),
    path('reexam/', views.reexam, name='reexam'),

    ]