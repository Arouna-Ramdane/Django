from django.shortcuts import render, redirect
from notes.forms.EnseignantForm import EnseignantForm

def add_enseignant(request):
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:enseignants')  
    else:
        form = EnseignantForm()
    return render(request, 'notes/add_enseignant.html', {'form': form})
