from django.shortcuts import render


# Create your views here.
def publication(request):
    dojin = "dojin"
    return render(request, 'publication.html',{"test":dojin})
    
def main(request):
    return render(request, 'main.html')