from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator

# Create your views here.
def job_list(request):
    job_list = Job.objects.all();
    #print(job_list);
    #return render(request,'html template',context);
    
    paginator = Paginator(job_list,1) # Show 25  contacts per page.
    page_number  = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    #context = {'jobs':job_list} # template name
    context = {'jobs':page_obj} # template name
    return render(request,'job/job_list.html',context)

def job_detail(request , slug):
    #pass
    job_detail = Job.objects.get(slug=slug);
    context = {'job' : job_detail}
    return render(request,'job/job_detail.html',context)


    
