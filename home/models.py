from django.db import models


# Create your models here.
class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)


class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)


