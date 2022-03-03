from django.db import models

# Create your models here.


class Exp(models.Model):
    title = models.CharField(max_length=255)
    team = models.CharField(max_length=255)
    description = models.TextField()
    gitHub =  models.URLField( null=True, blank=True)
    init_date = models.DateField()
    def __str__(self):
        return self.title

class Skills(models.Model):
    name = models.CharField(max_length=255)
    image =  models.URLField( null=True, blank=True)
    description = models.TextField()
    order = models.IntegerField()
    def __str__(self):
        return self.name


class Projects(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()

    gitHub =  models.URLField(blank=True)
    live =  models.URLField(blank=True)
    image =  models.URLField( null=True, blank=True)
    
    skills = models.ManyToManyField(Skills, related_name="projects")
    
    def __str__(self):
        return self.name

