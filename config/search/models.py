from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateTimeField("dob")

class Estimate(models.Model):
    pass
