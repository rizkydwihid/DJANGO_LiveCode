from django.shortcuts import render
from .models import Mentee

# Create your views here.
def pagedetail(request):
    detail = Mentee.objects.all()
    return render(request, 'mente/detail.html', {'detail':detail})