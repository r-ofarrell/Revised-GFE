from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateTimeField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    street = models.CharField(max_length=100)
    apt_bldg_ste = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)
    diagnosis = models.CharField(max_length=100, default=None, db_default=None)

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name}"
