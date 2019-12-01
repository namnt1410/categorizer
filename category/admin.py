from django.contrib import admin

# Register your models here.
from .models import Category, Language, Domain


admin.site.register(Language)


class DomainsInline(admin.TabularInline):
    model = Domain

# Define the admin class
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('tag', 'name')
    inlines = [DomainsInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(Domain) 
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'name', 'main_category', 
    	#'rank_alexa_global', 'rank_alexa_vietnam', 
    	'language', 'is_mobile', 'is_porn', 'is_malware', 'is_phishing')
    list_filter = ('main_category', 'language', 'is_mobile', 'is_porn', 'is_malware', 'is_phishing')
    search_fields = ('domain', 'name')