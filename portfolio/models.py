from django.db import models

class Welcome(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    image = models.ImageField(upload_to='welcome/')

class About(models.Model):
    description = models.TextField()

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()

class Education(models.Model):
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    year = models.IntegerField()

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()

class Award(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

class SocialLink(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

class Client(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='client/')

class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
