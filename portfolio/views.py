from django.shortcuts import render
from .models import Welcome, About, Skill, Education, Experience, Award, Service, SocialLink, Blog, Client, Testimonial, FAQ, Contact

# Create your views here.

def home(request):
    welcome = Welcome.objects.first()
    about = About.objects.first()
    skills = Skill.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    awards = Award.objects.all()
    services = Service.objects.all()
    social_links = SocialLink.objects.all()
    clients = Client.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'portfolio/home.html', {'welcome': welcome, 'about': about, 'skills': skills, 'education': education, 'experience': experience, 'awards': awards, 'services': services, 'social_links': social_links, 'clients': clients, 'testimonials': testimonials})

def blog(request):
    # Get all the blog posts
    posts = Blog.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'portfolio/blog.html', context)   


def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'portfolio/faq.html', {'faqs': faqs})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Send an email with the contact form details
        # send_mail(
        #     subject,
        #     f"Name: {name}\nEmail: {email}\nMessage: {message}",
        #     email,
        #     ['your_email@example.com'],  # Replace with your own email address
        #     fail_silently=False,
        # )

        # Render the contact confirmation page
        return render(request, 'portfolio/contact_confirm.html')

    return render(request, 'portfolio/contact.html')