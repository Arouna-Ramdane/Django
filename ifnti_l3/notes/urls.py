from django.urls import path
from . import views
from .views.eleve import *
from .views.matiere import *   
from .views.niveau import *
from .views.note import add_note
from .views.enseignant import *  
from .views.add_eleve import add_eleve
from .views.add_enseignant import add_enseignant

app_name="notes"
urlpatterns = [
	path('', views.index, name='index'),
    path('eleves/', views.eleves, name='eleves'),
    path('eleve/<int:id>/', views.eleve, name='eleve'),
    path('enseignants/', views.enseignants, name='enseignants'),
    path('enseignant/<int:id>/', views.enseignant, name='enseignant'),
    path('matieres/', views.matieres, name='matieres'),
    path('matiere/<int:id>/', views.matiere, name='matiere'),
    path('niveau/<int:id>/', views.niveau, name='niveau'),
    path('add_note/<int:eleve_id>/<int:matiere_id>/', add_note, name='add_note'),
    path('add_eleve/', add_eleve, name='add_eleve'),
    path('add_enseignant/', add_enseignant, name='add_enseignant'),

    path('update_eleve/<int:eleve_id>/', views.update_eleve, name='update_eleve'),
    path('update_enseignant/<int:enseignant_id>/', views.update_enseignant, name='update_enseignant'),

]
