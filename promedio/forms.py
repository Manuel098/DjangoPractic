from django import forms

from promedio.models import Materia
from promedio.models import Alumno

Li_Materia = (
    ([[e.id, e.name] for e in Materia.objects.all()])
)
Li_Alumno = (
    ([[e.id, e.name] for e in Alumno.objects.all()])
)


class AlMaForm(forms.Form):
    alumno = forms.ChoiceField(choices=Li_Alumno)
    calificacion = forms.CharField()
    materia = forms.ChoiceField(choices=Li_Materia)


class Maform(forms.Form):
    nombre = forms.CharField()


class Alform(forms.Form):
    alumno = forms.CharField()


class GetPromedio(forms.Form):
    nombreAlumno = forms.ChoiceField(choices=Li_Alumno)
