from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('',views.doctors_list,name='doctors_list'),
]
