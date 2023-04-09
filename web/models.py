from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255,)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

