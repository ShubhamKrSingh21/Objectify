from django.db import models
from PIL import Image
# Create your models here.


# Create your models here.
class FormModel(models.Model):
	img = models.ImageField(upload_to = "images/")

class SaveModel(models.Model):
	modeltype = models.TextField(default="")
	task = models.TextField() 
	choices = models.TextField(default="")    