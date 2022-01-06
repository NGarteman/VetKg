from django.db import models

class Vet(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    image =  models.ImageField(null=True, blank=True, upload_to="images/vets")
    experience = models.IntegerField(default=0)
    contacts = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.surname}"
