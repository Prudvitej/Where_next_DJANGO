from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    date = models.DateField()
    members = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.from_location} to {self.to_location})"
