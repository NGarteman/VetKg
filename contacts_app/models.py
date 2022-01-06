from django.db import models

class Contact(models.Model):
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    email = models.EmailField()


    def __str__(self):
            return f"ID:{self.id} ({self.phone_number})"

