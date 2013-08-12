from django.db import models

# Create your models here.
class Server(models.Model):
    name_server = models.CharField(max_length=50)
    place_server = models.CharField(max_length=50)
    flag_utilisation = models.CharField(max_length=50)
    ip_server = models.CharField(max_length=40)
    note_server = models.TextField(max_length=400)
