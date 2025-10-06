from django.shortcuts import render, get_object_or_404
from notes.models.Matiere import Matiere

# Create your views here.
from django.http import HttpResponse
def matieres(request):
    all_matieres = Matiere.objects.all()
    return render(request, "notes/matieres.html", {"all_matieres": all_matieres})

    # matieres = ""
    # for i in all_matieres :
    #     matieres += f"<h1>{i}</h1>"
    # return HttpResponse(matieres)

def matiere(request, id):
    une_matiere = get_object_or_404(Matiere, pk=id)
    return render(request, "notes/matiere.html", {"matiere": une_matiere})