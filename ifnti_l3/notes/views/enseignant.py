from django.shortcuts import render,get_object_or_404, redirect
from notes.models.Enseignant import Enseignant
from notes.forms import EnseignantForm

# Create your views here.
from django.http import HttpResponse
def enseignants(request):
    all_enseignants = Enseignant.objects.all()
    return render(request, "notes/enseignants.html", {"all_enseignants": all_enseignants})
    

def enseignant(request, id):
    enseignant = get_object_or_404(Enseignant, pk=id)
    return render(request, "notes/enseignant.html", {"enseignant": enseignant})
    

def update_enseignant(request, enseignant_id):
    enseignant = get_object_or_404(Enseignant, pk=enseignant_id)

    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect('notes:enseignant', id=enseignant.id)
    else:
        form = EnseignantForm(instance=enseignant)

    return render(request, 'notes/update_enseignant.html', {'form': form, 'enseignant': enseignant})