from django.db import models

class Image (models.Model):
	name = models.CharField(max_length=100)
	url= models.URLField(max_length=500)
	desc = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Contact(models.Model):
	name 	= models.CharField(max_length=250)
	email	= models.EmailField(max_length=200)
	phone	= models.CharField(max_length=20)
	comment	= models.TextField()

	def __str__(self):
		return self.name	