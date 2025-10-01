from django.db import models

class Personne(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=1, choices=[('F', 'Féminin'), ('M', 'Masculin')])
    date_naissance = models.DateField()

    class Meta:
        abstract = True

