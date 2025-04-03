from .models import Examen

def get_examenes():
    return Examen.objects.all().order_by('-fecha')[:10]

def create_examen(form):
    examen = form.save()
    examen.save()