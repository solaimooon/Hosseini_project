from django.db import models
from django.urls import reverse

class Facility(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='facility_icons/', blank=True, null=True)

    def __str__(self):
        return self.name


class Mosque(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    rigen = models.TextField()
    address = models.TextField()
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='mosques/logos/', blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    facilities = models.ManyToManyField('Facility', related_name='mosques', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mosque_detail', kwargs={'slug': self.slug})

class Hall(models.Model):
    mosque = models.ForeignKey(Mosque, related_name='halls', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    facilities = models.ManyToManyField('Facility', related_name='halls', blank=True)

    def __str__(self):
        return f"{self.name} ({self.mosque.name})"

class HallImage(models.Model):
    hall = models.ForeignKey(Hall, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='halls/images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.hall.name}"

