from django.shortcuts import render, get_object_or_404
from .models import Project, Skill, Contact, Image, Certification

from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models import Sum


# Helper Functions 

def get_context_from_projects(projects):
    # Helper function to extract relevant information from the projects queryset and return it in a dict
    
    context = { 
        'projects': [], 
        }
    
    for project in projects:
        context['projects'].append({
            'title': project.project_title,
            'slug': project.slug,
            'thumbnail': project.images.all().order_by('priority').first(), # The image with the highest priority is the thumbnail
            'short_description': project.short_description,
            'software_type': project.software_type,
            'lines_of_code': project.lines_of_code,
        })

    return context


# Views 

def index(request):
    # View for the /home page
    
    projects = Project.objects.all().filter(show_project=True).order_by('-featured', 'priority', '-end_date')[:3] # Retrieve the 3 most recent (based on end_date) Projects      
    context = get_context_from_projects(projects)
    
    return render(request, 'website/index.html', context) 


def about(request):
    # View for the /about page
    
    skills = Skill.objects.all().order_by('skill_type', 'priority')
    certifications = Certification.objects.all().order_by('priority')
    context = {
        "skills": skills, 
        "certifications": certifications,
    }

    return render(request, 'website/about.html', context)


def portfolio(request):
    # View for the /portfolio page
    
    projects = Project.objects.all().filter(show_project=True).order_by('-featured', 'priority', '-end_date') # Retrieve all the projects that are ordered by end_date
    context = get_context_from_projects(projects)

    context['lines_of_code'] = Project.objects.aggregate(total_lines_of_code=Sum('lines_of_code'))['total_lines_of_code']

    return render(request, 'website/portfolio.html', context)


def project(request, project_slug):
    # View for the /project page

    project = get_object_or_404(Project, slug = project_slug)
    images = project.images.all().order_by('priority')

    context = {
        'project': project, 
        'images': images,
    }

    return render(request, "website/project.html", context)


def contact(request):
    # View for the /contact page
    context = {}
    if request.method == 'POST':
        
        try:
            #it is possible that someone can submit only none by taking out the validation javascript
            #make sure you do not store none in everything
            form_first_name = request.POST.get('first_name')
            form_last_name = request.POST.get('last_name')
            form_email = request.POST.get('email')
            form_subject = request.POST.get('subject')
            form_message = request.POST.get('message')
            


            superusers_emails = User.objects.filter(is_superuser=True).values_list('email')
            recipient_list = []
            for x in superusers_emails:
                recipient_list.append(x[0])


            email_subject = 'New Submission via Contact @ yogipatel.dev'
            email_message = f'First Name: {form_first_name}\nLast Name: {form_last_name}\n\nEmail: {form_email}\n\nSubject: {form_subject}\n\nMessage:\n{form_message}'
            email_from = settings.EMAIL_HOST_USER
            send_mail( email_subject, email_message, email_from, recipient_list )
            
            contact = Contact(first_name=form_first_name, last_name=form_last_name, email=form_email, subject=form_subject, message=form_message)
            contact.save()


            context = {
                "show_success": True,
                "show_error": False,
            }
    
        except:
            context = {
                "show_success": False,
                "show_error": True,
            }
    
    else:
        context = {
                "show_success": False,
                "show_error": False,
            }
    
        

    return render(request, "website/contact.html", context)
