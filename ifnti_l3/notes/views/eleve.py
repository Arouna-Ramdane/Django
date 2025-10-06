from django.shortcuts import render,get_object_or_404
from notes.models.Eleve import Eleve
# Create your views here.
from django.http import HttpResponse
def eleves(request):
    all_eleves = Eleve.objects.all()
    return render(request, "notes/eleves.html", {"all_eleves": all_eleves})

    # eleves = ""
    # for i in all_eleves :
    #     eleves += f"<h1>{i}</h1>"
    # return HttpResponse(eleves)
    

def eleve(request, id):
    eleve = get_object_or_404(Eleve, pk=id)
    return render(request, "notes/eleve.html", {"eleve": eleve})

