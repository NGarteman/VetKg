from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=5000)
    image =  models.ImageField(null=True, blank=True, upload_to="images/news")

    def __str__(self):
            return f"ID:{self.id} ({self.title})"


class Price(models.Model):
    title = models.CharField(max_length=50)
    price_service = models.PositiveIntegerField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, related_name='service')

    def __str__(self):
            return f"ID:{self.id} ({self.title})"
