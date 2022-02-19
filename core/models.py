from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Exp(models.Model):
    title = models.CharField(max_length=255)
    team = models.CharField(max_length=255)
    description = models.TextField()
    gitHub =  models.URLField( null=True, blank=True)
    init_date = models.DateField()

    slug = models.SlugField(null=True, blank=True)



    def save(self, *args, **kwargs):
        slug = slugify(self.title) 
        self.slug = slug 
        super(Exp, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ["init_date"] 

    def __str__(self):
        return self.title


class Formation(models.Model):
    title = models.CharField(max_length=255)
    place = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    init_date = models.DateField()

    slug = models.SlugField(null=True, blank=True)

    
    class Meta:
        ordering = ["init_date"] 

    def save(self, *args, **kwargs):
        slug = slugify(self.title) 
        self.slug = slug 
        super(Formation, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Skills(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(null=True, upload_to='skills')
    description = models.TextField()

    slug = models.SlugField(null=True, blank=True)
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["order"] 

    def save(self, *args, **kwargs):
        slug = slugify(self.name) 
        self.slug = slug 
        super(Skills, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.order}- {self.name}"

class Projects(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()

    description = models.TextField()
    post = models.TextField(blank=True)

    gitHub =  models.URLField(blank=True)
    live =  models.URLField(blank=True)

    image = models.FileField(null=True, blank=True, upload_to='projects')
    
    skills = models.ManyToManyField(Skills, related_name="projects")
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name) 
        self.slug = slug 
        super(Projects, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    


