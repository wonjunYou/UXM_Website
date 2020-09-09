from django.shortcuts import render

def base(request):
    return render(request, 'introduce/base.html')

def main(request):
    return render(request, 'main.html')