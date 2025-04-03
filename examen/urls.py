from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('examenes/', views.examen_list),
    path('examencreate/', csrf_exempt(views.examen_create), name='examenCreate'),
]