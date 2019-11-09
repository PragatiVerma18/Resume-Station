from django.urls import path,include
from . import views
from . views import GeneratePdf

urlpatterns = [
 path('create', views.create, name='create'),
 path('resume', views.resume, name='resume'),
 path('pdf', GeneratePdf.as_view(), name='pdf'),

]