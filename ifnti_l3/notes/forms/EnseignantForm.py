from django import forms
from notes.models import Enseignant

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom', 'sexe', 'date_naissance']
        labels = {
            'nom': "Nom de l'enseignant",
            'prenom': "Prénom de l'enseignant",
            'sexe': "le sexe de l'enseignant",
            'date_naissance': "date de naissance de l'enseignant",
        }
