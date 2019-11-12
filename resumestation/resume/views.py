from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
def home(request):
  return render(request, 'resume/home.html')

@login_required
def create(request):
  if request.method == 'POST':
    details = json.loads(request.POST['hidden-input-details'])
    username = details['username'][0]
    title = details['title'][0]
    about = details['about'][0]
    
    personalSkills = json.loads(request.POST['hidden-input-skills1'])['skills1']
    level = json.loads(request.POST['hidden-input-skills1'])['skills1_level']

    professionalSkills = json.loads(request.POST['hidden-input-skills2'])['skills2']
    score = json.loads(request.POST['hidden-input-skills2'])['skills2_level']

    skills1 = list(zip(personalSkills, level))
    skills2 = list(zip(professionalSkills, score))

    start = json.loads(request.POST['hidden-input-education'])['start']
    end = json.loads(request.POST['hidden-input-education'])['end']
    course = json.loads(request.POST['hidden-input-education'])['course']
    institution = json.loads(request.POST['hidden-input-education'])['institution']
    description = json.loads(request.POST['hidden-input-education'])['description']

    education = list(zip(start, end, course, institution, description))

    workStarted = json.loads(request.POST['hidden-input-work'])['start']
    workEndDate = json.loads(request.POST['hidden-input-work'])['end']
    company = json.loads(request.POST['hidden-input-work'])['company']
    designation = json.loads(request.POST['hidden-input-work'])['designation']
    description = json.loads(request.POST['hidden-input-work'])['description']

    work = list(zip(workStarted, workEndDate, company, designation, description))

    context = {
      'username': username, 'title': title, 'about': about, 'skills1': skills1, 'skills2': skills2, 'education': education, 'work': work
    }
    
    return render(request, 'resume/resume.html', context)
  else:
    return render(request, 'resume/create.html')

def resume(request):
  return render(request, 'resume/resume.html')
