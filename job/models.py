from django.db import models
from django.utils.text import slugify

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

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    #return "jobs/%s/%s.%s"%(instance.id,instance.id,extension)
    return "jobs/%s.%s"%(instance.id,extension)
    
    
class Job(models.Model): #table
    title = models.CharField(max_length=100); #column
    #location 
    job_type = models.CharField(max_length=15, choices=JOB_TYPE);#models
    description = models.TextField(max_length=1000);#description
    published_at = models.DateTimeField(auto_now=True);#publish_at
    Vacancy = models.IntegerField(default=1);#Vacancy
    salary = models.IntegerField(default=0);#salary
    experience = models.IntegerField(default=1);#experience
    category = models.ForeignKey('Category', on_delete=models.CASCADE);#category
    #image = models.ImageField(upload_to='jobs/')
    image = models.ImageField(upload_to=image_upload)
    
    slug = models.SlugField(blank=True, null=True) #slug
    
    
    def save(self,*args,**kwargs):
        
        self.slug = slugify(self.title) ##logic 
        
        super(Job,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title;
    

class Category(models.Model):
    name =  models.CharField(max_length=25);
    
    def __str__(self):
        return self.name
    
class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name