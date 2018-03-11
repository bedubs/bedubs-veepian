from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('make-cert/', views.make_cert, name='make-cert'),
]
