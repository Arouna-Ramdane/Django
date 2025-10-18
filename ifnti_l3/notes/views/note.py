from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from notes.models import Eleve, Matiere, Note, Niveau
from notes.forms import NoteForm

def add_note(request, eleve_id, matiere_id):
    eleve = get_object_or_404(Eleve, pk=eleve_id)
    matiere = get_object_or_404(Matiere, pk=matiere_id)
    niveau_eleve = get_object_or_404(Niveau, nom=eleve.niveau)

    if niveau_eleve not in matiere.niveau.all():
        return HttpResponse(f"L'élève {eleve} ne suit pas la matière {matiere.nom}.")

    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.eleve = eleve
            note.matiere = matiere
            note.save()
            return redirect('notes:eleve', id=eleve.matricule)
    else:
        form = NoteForm()

    return render(request, 'notes/add_Note.html', {'form': form, 'eleve': eleve, 'matiere': matiere})


    # if request.method == "POST":
    #     valeur = request.POST.get("valeur")
    #     Note.objects.create(eleve=eleve, matiere=matiere, valeur=valeur)
    #     return render(request, "notes/add_Note.html", {"eleve": eleve, "matiere": matiere})
    # return render(request, "notes/add_Note.html", {"eleve": eleve, "matiere": matiere})