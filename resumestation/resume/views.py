from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import json

# Create your views here.
def home(request):
  return render(request, 'resume/home.html')

@login_required
def create(request):
  if request.method == 'POST':
    data = request.POST['data']
    y = json.loads(data)
    print(y)
  
  return render(request, 'resume/create.html')