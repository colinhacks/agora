from django.db import models
from django.contrib import admin


# Create your models here.
class City(models.Model):
	name = models.CharField(max_length=100)
	mayor = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name + ", whose mayor is "+self.mayor

admin.site.register(City)