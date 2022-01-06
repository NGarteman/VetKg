from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
            return f"{self.name}"


class Record(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    accept = models.BooleanField(default=False)


    def __str__(self):
            return f"ID:{self.id} ({self.name}, {self.phone_number})"


