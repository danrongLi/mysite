from django.db import models

from django.utils.translation import gettext as _


class Pet(models.Model):

    name = models.CharField(
            help_text=_('Name of Animal'),
            max_length=50,
    )


    species = models.CharField(
           help_text=_('Species of Animal'),
            max_length=100,
    )

    birth_date = models.DateField(
            help_text=_('Birth Date'),
    )

    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'

    SEX_CHOICES=(
            (MALE, 'Male'),
            (FEMALE, 'Female'),
            (OTHER, 'Other'),
           
    )

    sex = models.CharField(
            help_text=_('Sex of the pet'),
            max_length=35,
            choices=SEX_CHOICES,
            default=OTHER,
    )

    def __str__(self):
        return self.name




# Create your models here.
