from django.db import models
from django.contrib.auth.models import User


class Workspace(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    has_wifi = models.BooleanField(default=False)
    is_quiet = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' - ' + self.workspace.name
