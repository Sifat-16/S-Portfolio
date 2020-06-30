from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm
# Create your views here.

def home(request):
    profile = Profile.objects.all().order_by('-id')[0]

    facts = Facts.objects.all()
    skill = Skills.objects.all()
    rs = ResumeSummery.objects.all().order_by('-id')[0]
    education = Education.objects.all()
    profession = ProfessionalExperience.objects.all()
    portfolio = Portfolio.objects.all()
    category = Category.objects.all()
    testimony = Testimonial.objects.all()

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')

    else:
        form = ContactForm()

    context = {'profile': profile, 'facts': facts, 'skill': skill, 'rs': rs, 'education': education, 'profession': profession, 'portfolio': portfolio, 'category': category, 'testimony': testimony, 'form': form}
    return render(request, 'index.html', context)




def port(request, port_slug):
    port = Portfolio.objects.get(slug=port_slug)
    profile = Profile.objects.all().order_by('-id')[0]

    context = {'port': port, 'profile': profile}
    return render(request, 'portfolio-details.html', context)