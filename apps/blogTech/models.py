from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, null=True, blank=True, unique=True)
    ordering = models.IntegerField(null=True, blank=True)
    pather = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE)

    def isCategory(self):
        if self.pather:
            return "SubCategory"
        else:
            return "Category"
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['ordering']



class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, null=True, blank=True, unique=True)
    content = models.TextField()

    ordering = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['ordering']
    def __str__(self):
        return self.title