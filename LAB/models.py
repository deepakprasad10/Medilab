from django.db import models
# Create your models here.


class Appointment(models.Model):
    Your_Name = models.CharField(max_length=50)
    Your_Email = models.EmailField(max_length=100)
    Subject = models.CharField(max_length=100)
    Message = models.TextField()

    def __str__(self):
        return self.Your_Name
