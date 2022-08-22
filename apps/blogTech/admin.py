from django.contrib import admin
from .models import Article, Category
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "category")

    search_fields = ['category__title']
    def get_search_results(self, request, queryset, search_term):
        print("In get search results")
        results = super().get_search_results(request, queryset, search_term)
        return results
    autocomplete_fields = ['category']


@admin.register(Category)
class CategoryAdmind(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ( "title", "isCategory", "pather")
    search_fields = ['title']
    def get_search_results(self, request, queryset, search_term):
        print("In get search results")
        results = super().get_search_results(request, queryset, search_term)
        return results
    autocomplete_fields = ['pather']
    
