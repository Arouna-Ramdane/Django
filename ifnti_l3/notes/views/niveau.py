from django.shortcuts import render,get_object_or_404
from notes.models.Niveau import Niveau

# Create your views here.
from django.http import HttpResponse
def niveau(request, id):
    niveau = get_object_or_404(Niveau, pk=id)
    return render(request, "notes/niveau.html", {"niveau": niveau})
