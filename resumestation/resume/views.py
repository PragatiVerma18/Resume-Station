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
    username = request.POST['username']
    title = request.POST['title']
    about = request.POST['about']
    personal_skills = request.POST['personal-skills']
    personal_skills_percentage = request.POST['personal-skills-percentage']
    professional_skills = request.POST['professional-skills']
    professional_skills_percentage = request.POST['professional-skills-percentage']
    work_started = request.POST['work-started'] 
    work_end_date = request.POST['work-end-date']
    company = request.POST['company']
    designation = request.POST['designation']
    description = request.POST['description']
    started = request.POST['started']
    end_date = request.POST['end-date']
    course = request.POST['course']
    institution = request.POST['course']
    education_description = request.POST['education-description']

    context = {'username': username, 'title':title, 'about':about, 'personalskills':personal_skills, 'personalskillspercentage':personal_skills_percentage, 'professionalskills':professional_skills, 'professionalskillspercentage': professional_skills_percentage, 'workstarted':work_started, 'workenddate':work_end_date, 'company':company, 'designation':designation, 'description':description, 'started':started, 'enddate':end_date, 'course': course, 'institution':institution, 'educationdescription':education_description }
    
    return render(request, 'resume/resume.html', context)
  else:
    return render(request, 'resume/create.html')

def resume(request):
  return render(request, 'resume/resume.html')

from django.http import HttpResponse
from django.views.generic import View

from .utils import render_to_pdf #created in step 4

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('pdf/resume.html')
        return HttpResponse(pdf, content_type='application/pdf')