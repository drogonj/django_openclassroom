from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    def __str__(self):
        return f'{self.name}'
    class Danger_level(models.TextChoices):
        NON_SPECIFIED = 'UWN'
        SAFE = 'SFE'
        LOW = 'LOW'
        MED = 'MED'
        HIGH = 'S'
        S_HIGH = 'SS'
        EXTREME = 'SSS'
    name = models.fields.CharField(max_length=100)
    danger_level = models.fields.CharField(choices=Danger_level.choices, max_length=3, default=Danger_level.NON_SPECIFIED)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1800), MaxValueValidator(2024)],
        default=2000
    )
    active = models.fields.BooleanField(default=True)
    biography = models.fields.CharField(max_length=1000, default="")
    official_homepage = models.fields.URLField(null=True, blank=True, max_length=200)

class Announce(models.Model):
    title = models.fields.CharField(max_length=100)

class Contact(models.Model):
    firstname = models.fields.CharField(max_length=50)
    lastname = models.fields.CharField(max_length=50)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    localisation = models.fields.CharField(max_length=100)