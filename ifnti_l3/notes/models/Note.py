from django.db import models
from .Matiere import Matiere
from .Eleve import Eleve


class Note(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    valeur = models.FloatField(null=True)

    def __str__(self):
        return f"{self.eleve} {self.matiere} {self.valeur}"