from django.shortcuts import render
from .forms import PacientesForm
# Create your views here.
from django.contrib import messages
from .models import Pacientes

def index(request):
    return render(request ,"pacientes/index.html")

def registrar(request):
    contex = {
        "form": PacientesForm
    }

    if request.method == "POST":
        formulario = PacientesForm(data=request.POST)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Se registro el paciente")
        else:
            contex["form"] = formulario
            

    return render(request ,"pacientes/registrar.html", contex)

def listado(request):
    context = {
        "pacientes":  Pacientes.objects.all()
    }
    messages.success(request, "listado de pacientes")


    return render(request ,"pacientes/listado.html", context)
    