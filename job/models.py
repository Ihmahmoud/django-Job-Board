from django.db import models

# Create your models here.


'''
django model field :
    - html widget
    - validation
    - db size
    
'''

JOB_TYPE = (
    ('FULL Time','FULL Time'),
    ('PART Time','PART Time'),
)
class Job(models.Model): #table
    title = models.CharField(max_length=100); #column
    #location 
    job_type = models.CharField(max_length=15, choices=JOB_TYPE);#models
    description = models.TextField(max_length=1000);#description
    published_at = models.DateTimeField(auto_now=True);#publish_at
    Vacancy = models.IntegerField(default=1);#Vacancy
    salary = models.IntegerField(default=0);#salary
    #category
    experience = models.IntegerField(default=1);#experience
    
    
    def __str__(self):
        return self.title;
    