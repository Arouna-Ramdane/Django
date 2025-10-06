from django.urls import path
from . import views
from .views.eleve import *
from .views.matiere import *   
from .views.niveau import *   

app_name="notes"

urlpatterns = [
	path('', views.index, name='index'),
    path('eleves/', views.eleves, name='eleves'),
    path('eleve/<int:id>/', views.eleve, name='eleve'),
    path('matieres/', views.matieres, name='matieres'),
    path('matiere/<int:id>/', views.matiere, name='matiere'),
    path('niveau/<int:id>/', views.niveau, name='niveau'),
]
