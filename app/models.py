from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
    """
    Base model for all models
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Individual(BaseModel):
    """
    Individual / Person model
    """
    name = models.CharField(max_length=255)


class Faith(BaseModel):
    """

    """
    name = models.CharField(max_length=255)


class Location(BaseModel):
