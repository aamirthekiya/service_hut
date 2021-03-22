from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
class Document(models.Model):
	name = models.CharField(max_length=50)
	keyword = models.CharField(max_length=1024)
	file = models.FileField(upload_to='documents/')
	creater = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def abc(self):
		name , extension = os.path.splitext(self.file.name)
		if extension == 'doc':
			return '.doc'
		else:
			return '.docx'
