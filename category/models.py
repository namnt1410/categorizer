from django.db import models

# Create your models here.

class Category(models.Model):
    """Model representing a category (e.g. Search Engines & Portals, Computers & Technology etc.)."""
    tag = models.CharField(
        max_length=200,
        help_text="Enter a category tag (e.g. search_engine_and_portals, computers_and_technology etc.)",
        unique=True
        )
    name = models.CharField(
        max_length=200,
        help_text="Enter a category name (e.g. Search Engines & Portals, Computers & Technology etc.)"
        )

    class Meta:
        ordering = ['tag', 'name']

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200,
                            help_text="Enter the domain language (e.g. English, French, Japanese etc.)",
                            unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Domain(models.Model):
    """Model representing a domain (e.g. vnexpress.net, facebook.com, google.com, etc.)"""
    domain = models.CharField(max_length=200,
                              help_text="Enter the domain (e.g. vnexpress.net, facebook.com, google.com, etc.)",
                              unique=True)
    name = models.CharField(max_length=200,
                            help_text="Enter the domain title (e.g. Vnexpress, Facebook, Google, etc.)")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    #rank_alexa_global = models.IntegerField(
    #	help_text="Enter the global Alexa rank", blank=True)
    #rank_alexa_vietnam = models.IntegerField(help_text="Enter the Vietnam Alexa rank", blank=True)
    main_category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    is_foreign = models.BooleanField(help_text="Select if domain is foreign site")
    is_mobile = models.BooleanField(help_text="Select if domain is mobile site")
    is_porn = models.BooleanField(help_text="Select if domain is porn")
    is_malware = models.BooleanField(help_text="Select if domain is malware")
    is_phishing = models.BooleanField(help_text="Select if domain is phishing")

    class Meta:
        ordering = ['domain']

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name