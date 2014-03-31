from django.db import models

from coco.base_models import GENDER_CHOICES
from geographies.models import Block, Village
from programs.models import Partner


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __unicode__(self):
        return self.name


class Trainee(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    village = village = models.ForeignKey(Village)
    partner = models.ForeignKey(Partner)

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ("name", "village")


class Donor(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Training(models.Model):
    date = models.DateField()
    block = models.ForeignKey(Block)
    donor = models.ForeignKey(Donor)
    partner = models.ForeignKey(Partner)
    module = models.ForeignKey(Module)
    days = models.FloatField()
    trainers = models.ManyToManyField(Trainer)
    trainees = models.ManyToManyField(Trainee, through='TraineeTrained')

    def __unicode__(self):
        return self.date


class TraineeTrained(models.Model):
    training = models.ForeignKey(Training)
    trainee = models.ForeignKey(Trainee)
    environmen_creation_grade = models.FloatField()
    facilitation_grade = models.FloatField()
    pico_handling_documentation_grade = models.FloatField()
