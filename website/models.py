from django.db import models
from rezervation.models import *
from django.utils.text import slugify
from autoslug import AutoSlugField
from django_jalali.db import models as jmodels

class Category(models.Model):
    mosque = models.ForeignKey('rezervation.Mosque', on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
    image = models.ImageField("media_category_picture")

    # SEO Fields
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.name} - {self.mosque.name}"


class Occasion(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="occasions")
    name = models.CharField(max_length=200,help_text="مناسبت + سال مثال : دهه اول ماه محرم 1404")
    year = models.IntegerField()
    slug = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media_night',default='null')

    # SEO Fields
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # اگر slug خالی بود یا می‌خواهیم همیشه از name ساخته شود
        if self.name:
            self.slug = self.name
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.year}"

class style_media_file(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Night(models.Model):
    occasion = models.ForeignKey(Occasion, on_delete=models.CASCADE, related_name="nights")
    number = models.IntegerField(null=True,blank=True)
    slug = models.CharField(max_length=100 ,help_text="این فیلد به عنوان نام شب هم در کد استفاده شده است ")
    image = models.ImageField(upload_to='media_night',default='null')

    # SEO Fields
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"شب {self.number} - {self.occasion}"


class owner(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"



class MediaFile(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('audio', 'Audio'),
        ('video', 'Video'),
    ]
    night = models.ForeignKey(Night, on_delete=models.CASCADE, related_name="media_files")
    file = models.FileField(upload_to='media/')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media_night',default='null')
    style_media_file = models.ForeignKey(style_media_file,on_delete=models.SET_NULL,null=True,blank=True)
    owner=models.ForeignKey(owner,on_delete=models.SET_NULL,null=True,blank=True)
    date = jmodels.jDateField(null=True,blank=True)
    Selected = models.BooleanField(null=True,blank=True)

    # SEO Fields
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title




# Create your models here.
