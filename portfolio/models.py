from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)

    short = models.TextField()
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='about/')
    main = RichTextField()
    shortkey = models.CharField(max_length=30, blank=True, null=True)
    facebook = models.URLField(max_length=50, blank=True, null=True)
    twittr = models.URLField(max_length=50, blank=True, null=True)
    instagram = models.URLField(max_length=50, blank=True, null=True)
    linkedin = models.URLField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

class Facts(models.Model):
    short = models.TextField(blank=True, null=True)
    number = models.IntegerField()
    keyword = models.TextField()

    def __str__(self):
        return self.keyword

class Skills(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()

    def __str__(self):
        return self.name

class ResumeSummery(models.Model):
    description = RichTextField()

    def __str__(self):
        return self.description

class Education(models.Model):
    title = models.CharField(max_length=50)
    time_from = models.DateField()
    time_till = models.DateField()
    institute = models.CharField(max_length=100)
    description = RichTextField()

    def __str__(self):
        return self.title

class ProfessionalExperience(models.Model):
    title = models.CharField(max_length=50)
    time_from = models.DateField()
    time_till = models.CharField(max_length=10, blank=True, null=True)

    institute = models.CharField(max_length=100)
    description = RichTextField()

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='portfolio', blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    client = models.CharField(max_length=50)
    project_date = models.DateField()
    project_url = models.URLField(max_length=100, blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique_with='project_date')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=50)
    testimonial = RichTextField()
    image = models.ImageField(upload_to='testimonial/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name
