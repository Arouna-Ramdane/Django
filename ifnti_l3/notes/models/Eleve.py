from .Personne import Personne
from django.db import models
from .Niveau import Niveau



class Eleve(Personne):
    matricule = models.AutoField(primary_key=True)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    class Meta:
        verbose_name = "Élève"
        verbose_name_plural = "Élèves"
