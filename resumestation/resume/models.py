from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
  name = models.ForeignKey(User, on_delete= models.CASCADE)
  title = models.CharField(max_length=50)
  about = models.CharField(max_length=255)
  personal_skill1 = models.CharField(max_length=20)
  personal_skill2 = models.CharField(max_length=20)
  personal_skill3 = models.CharField(max_length=20)
  personal_skill4 = models.CharField(max_length=20)
  personal_skill1_bar1 = models.IntegerField()
  personal_skill1_bar2 = models.IntegerField()
  personal_skill1_bar3 = models.IntegerField()
  personal_skill1_bar4 = models.IntegerField()
  professional_skill1 = models.CharField(max_length=20)
  professional_skill2 = models.CharField(max_length=20)
  professional_skill3 = models.CharField(max_length=20)
  professional_skill4 = models.CharField(max_length=20)
  professional_skill1_bar1 = models.IntegerField()
  professional_skill1_bar2 = models.IntegerField()
  professional_skill1_bar3 = models.IntegerField()
  professional_skill1_bar4 = models.IntegerField()
  education_time1 = models.DateField(auto_now=False)
  education_time2 = models.DateField(auto_now=False)
  education_time3 = models.DateField(auto_now=False)
  education_time4 = models.DateField(auto_now=False)
  education_comp1 = models.CharField(max_length=50)
  education_comp2 = models.CharField(max_length=50)
  education_comp3 = models.CharField(max_length=50)
  education_comp4 = models.CharField(max_length=50)
  education_des1 = models.CharField(max_length=80)
  education_des2 = models.CharField(max_length=80)
  education_des3 = models.CharField(max_length=80)
  education_des4 = models.CharField(max_length=80)
  
  work_time1 = models.DateField(auto_now=False)
  work_time2 = models.DateField(auto_now=False)
  work_time3 = models.DateField(auto_now=False)
  work_time4 = models.DateField(auto_now=False)
  work_comp1 = models.CharField(max_length=50)
  work_comp2 = models.CharField(max_length=50)
  work_comp3 = models.CharField(max_length=50)
  work_comp4 = models.CharField(max_length=50)
  work_des1 = models.CharField(max_length=80)
  work_des2 = models.CharField(max_length=80)
  work_des3 = models.CharField(max_length=80)
  work_des4 = models.CharField(max_length=80)

  


  def __str__(self):
    return self.name

  def pub_date_pretty(self):
    return self.pub_date.strftime('%b %e %Y')