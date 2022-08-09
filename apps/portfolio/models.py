from distutils.command.upload import upload
from email.mime import image
from statistics import mode
from django.db import models

# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=100)
    svg = models.TextField()
    description = models.TextField()
    color = models.CharField(max_length=10)  # fffff


class Work(models.Model):  # Ultimos trabajos realizados trabajos realizados layout y frelance
    # TODO ordenar por id osea edicion
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='works')
    live = models.URLField(null=True, blank=True)

    place = models.CharField(max_length=255)
    place_web = models.URLField(null=True, blank=True)

    my_title = models.CharField(max_length=255)
    description = models.TextField()

    init_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)


    skills = models.ManyToManyField(Skill, related_name="works")

    def __str__(self):
        return self.name


class Project(models.Model):  # proyectos personales

    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='projets')
    live = models.URLField(null=True, blank=True)


    init_date = models.DateField()

    intro = models.TextField()
    description = models.TextField()  # blog

    skills = models.ManyToManyField(Skill, related_name="projects")

    def __str__(self):
        return self.name
