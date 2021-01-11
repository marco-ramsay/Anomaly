from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Anomaly, Project
from .forms import GeneralForm, UpdateForm

# Create your views here.
def index(request):
    return render(request, 'anomalyapp/index.html')


def projects(request):
    projects = Project.objects.all()
    return render(request, 'anomalyapp/projects.html', {'projects':projects})


def main(request, pk):
    project = Project.objects.get(id=pk)
    anomaly = project.anomaly_set.all()
    total_anomalies = anomaly.count()
    signed = anomaly.filter(review_status='Client_signed').count()
    not_signed = anomaly.filter(review_status='Not_Signed').count()
    context = {'project':project, 'anomaly':anomaly, 'total_anomalies':total_anomalies, 'signed':signed, 'not_signed':not_signed}
    return render(request, 'anomalyapp/anom-main.html', context)


def anom(request, pk):
    anomaly = Anomaly.objects.get(id=pk)
    return render(request, 'anomalyapp/anom-id.html', {'anomaly':anomaly})


def createAnomaly(request):
    form = GeneralForm()
    if request.method == 'POST':
        print('printing POST:', request.POST)
        form = GeneralForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        else:
            return redirect('projects')

    context = {'form':form}
    return render(request, 'anomalyapp/form.html', context)


def updateAnomaly(request, pk):
    anomaly = Anomaly.objects.get(id=pk)
    form = UpdateForm(instance=anomaly)
    if request.method == 'POST':
        print('printing POST:', request.POST)
        form = UpdateForm(request.POST , request.FILES, instance=anomaly)
        if form.is_valid():
            form.save()
        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        else:
            return redirect('projects')

    context = {'form':form}
    return render(request, 'anomalyapp/update.html', context)


def deleteAnomaly(request, pk):
    anomaly = Anomaly.objects.get(id=pk)
    if request.method == 'POST':
        anomaly.delete()
        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        else:
            return redirect('projects')

    context = {'item':anomaly}
    return render(request, 'anomalyapp/delete.html', context)


def render_pdf_anom(request, *args, **kwargs):
    pk = kwargs.get('pk')
    anomaly = get_object_or_404(Anomaly, pk=pk)
    template_path = 'anomalyapp/pdf_test.html'
    context = {'anomaly': anomaly}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def export(request, pk):
    project = Project.objects.get(id=pk)
    anomaly = project.anomaly_set.all()
    return render(request, 'anomalyapp/export.html', {'anomaly':anomaly})
