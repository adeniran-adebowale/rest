from  django.urls import path
from . import views



urlpatterns= [
    path('',views.home, name='mobileApp Home'),
    path('features/',views.features, name='features'),

]