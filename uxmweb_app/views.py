from django.shortcuts import render


# Create your views here.
def publication(request):
    dojin = "dojin"
    return render(request, 'publication.html',{"test":dojin})
def project(request):
    pj = "pj"
    return render(request, 'project.html',{"pj":pj})
def main(request):
    return render(request, 'main.html')