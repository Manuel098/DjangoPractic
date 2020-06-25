from django.shortcuts import render
from django.http import HttpResponse
from .forms import AlMaForm, Maform, Alform, GetPromedio

from promedio.models import Materia, Alumno, AlMa


def index(request):
    alMaForm = AlMaForm()
    maform = Maform()
    alform = Alform()
    globalProm = '0'

    promed = GetPromedio()
    if request.method == 'POST':
        form1 = AlMaForm(request.POST)
        form2 = Maform(request.POST)
        form3 = Alform(request.POST)
        form4 = GetPromedio(request.POST)

        if form1.is_valid():
            g_alumn = form1.cleaned_data['alumno']
            g_cali = form1.cleaned_data['calificacion']
            g_mat = form1.cleaned_data['materia']

            setData({
                'k_materia': g_mat,
                'k_alumno': g_alumn,
                'calif': g_cali
            }, AlMa)
        elif form2.is_valid():
            setData({
                'name': form2.cleaned_data['nombre'],
            }, Materia)
        elif form3.is_valid():
            setData({
                'name': form3.cleaned_data['alumno'],
            }, Alumno)
        elif form4.is_valid():
            globalProm = str(getProm(form4.cleaned_data['nombreAlumno']))
    return render(request, 'index.html', {'promed': globalProm, 'Calif': AlMa.objects.all(), 'alMaform': alMaForm, 'maform': maform, 'alform': alform, 'prom': promed})


def setData(data, obje):
    if obje == AlMa:
        p = obje.objects.create(
            k_materia=Materia.objects.filter(id=data['k_materia'])[0],
            k_alumno=Alumno.objects.filter(id=data['k_alumno'])[0],
            calif=data['calif']
        )
    else:
        p = obje.objects.create(
            name=data['name']
        )


def getProm(userId):
    g_list = AlMa.objects.filter(k_alumno_id=userId)
    promedio = 0

    for item in g_list:
        promedio += item.calif

    promedio /= len(g_list)
    return promedio
