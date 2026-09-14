from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *
from .forms import ContactForm


def home(request):
    services = Service.objects.filter(
        is_active=True
    )[:3]

    projects = Project.objects.filter(
        is_featured=True
    )[:3]

    team_members = TeamMember.objects.filter(
        is_active=True
    )[:4]

    testimonials = Testimonial.objects.filter(
        is_active=True
    )[:3]

    statistics = SiteStatistic.objects.filter(
        is_active=True
    )[:4]

    context = {
        'services': services,
        'projects': projects,
        'team_members': team_members,
        'testimonials': testimonials,
        'statistics': statistics,
    }

    return render(
        request,
        'core/home.html',
        context
    )


def about(request):
    return render(
        request,
        'core/about.html'
    )


def services(request):
    services = Service.objects.filter(
        is_active=True
    )

    return render(
        request,
        'core/services.html',
        {
            'services': services
        }
    )


def projects(request):
    projects = Project.objects.all()

    return render(
        request,
        'core/projects.html',
        {
            'projects': projects
        }
    )

def project_detail(request, pk):

    project = Project.objects.get(pk=pk)

    return render(
        request,
        'core/project_detail.html',
        {
            'project': project
        }
    )



def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Thank you! Your message has been sent successfully.'
            )

            return redirect('contact')

    else:
        form = ContactForm()

    return render(
        request,
        'core/contact.html',
        {
            'form': form
        }
    )

def team(request):

    team_members = TeamMember.objects.filter(
        is_active=True
    )

    return render(
        request,
        'core/team.html',
        {
            'team_members': team_members
        }
    )

