from django.urls import path
from . import views

urlpatterns = [
    path('detail', views.pagedetail, name='detail'),
]
