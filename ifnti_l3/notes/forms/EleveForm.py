from django import forms
from notes.models import Eleve

class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = ['nom', 'prenom', 'sexe', 'date_naissance', 'matricule', 'niveau']
        labels = {
            'nom': "Nom de l'élève",
            'prenom': "Prénom de l'élève",
            'sexe': "le sexe de l'élève",
            'date_naissance': "date de naissance de l'élève",
            'matricule': "telephone de l'élève",
            'niveau': "niveau de l'élève",
        }

