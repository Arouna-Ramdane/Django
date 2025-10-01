from .Personne import Personne
from django.db import models



class Enseignant(Personne):
    pass

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    class Meta:
        verbose_name = "Enseignant"
        verbose_name_plural = "Enseignants"