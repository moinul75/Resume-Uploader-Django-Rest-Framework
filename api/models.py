from django.db import models


# Create your models here.
state_choice = ((
    ('Brahmanbaria','Brahmanbaria'),
    ('Cummilla','Cummilla'),
    ('Feni','Feni'),
    ('Laxmipur','Laxmipur'),
    ('Noakhali','Noakhali'),
    ('Chittagong','Chittagong'),
    ('Coxsbazar','Coxsbazar'),
    ('Faridpur','Faridpur'),
    ('Khulna','Khulna'),
    ('Rajshahi','Rajshahi')
))

#Profile for submiting Resume for the candidate 
class Profile(models.Model):
    name = models.CharField(blank=False,max_length=100)
    email = models.EmailField(blank=False)
    dob = models.DateField(blank=False,auto_now_add=False)
    state = models.CharField(choices=state_choice,blank=False,max_length=100)
    gender = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='Profile_Image',blank=True)
    resume_doc = models.FileField(blank=True,upload_to='Resume_files')
    
    
    
 
 
    
