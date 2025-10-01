from django.db import models
from .Niveau import Niveau
from .Enseignant import Enseignant
from .Eleve import Eleve


class Matiere(models.Model):
    nom = models.CharField(max_length=50, unique=True)
    niveau = models.ManyToManyField(Niveau)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, null=True, blank=True)
    eleve = models.ManyToManyField(Eleve)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Matière"
        verbose_name_plural = "Matières"
