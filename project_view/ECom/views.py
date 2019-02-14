from django.shortcuts import render

# Create your views here.
def pagehome(request):
    return render(request, 'homepage/home.html', {})

def pagedetail(request):
    return render(request, 'homepage/detail.html', {})