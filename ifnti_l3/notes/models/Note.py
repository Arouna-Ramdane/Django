from django.db import models
from .Matiere import Matiere
from .Eleve import Eleve
from django.core.validators import MinValueValidator, MaxValueValidator


class Note(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    valeur = models.FloatField(
        validators=[
            MinValueValidator(0), 
            MaxValueValidator(20)
        ],default=0)

    def __str__(self):
        return f"{self.eleve} {self.matiere} {self.valeur}"