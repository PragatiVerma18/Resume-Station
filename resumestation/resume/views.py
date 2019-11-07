from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'resume/home.html')

def create(request):
  return render(request, 'resume/create.html')