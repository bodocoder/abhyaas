from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='10q'),
    path('result/',views.result, name='10q-result'),
]
