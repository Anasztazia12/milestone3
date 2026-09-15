from django.db import models
from django.contrib.auth.models import User


class Cafe(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    has_power_outlets = models.BooleanField(default=True)
    wifi_speed_mbps = models.IntegerField(default=50)
    quiet_rating = models.IntegerField(default=3)
    members_only = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " (" + self.city + ")"


class Spot(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    spot_name = models.CharField(max_length=100)
    capacity = models.IntegerField(default=1)

    def __str__(self):
        return self.cafe.name + ' - ' + self.spot_name


class Booking(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')

    def __str__(self):
        return self.user.username + ' - ' + self.spot.cafe.name + ' (' + str(self.date) + ')'
