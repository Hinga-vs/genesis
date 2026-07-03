from django.db import models

# Create your models here.
class contact1(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    time = models.DateTimeField()

   


    def __str__(self):
      return self.name
    