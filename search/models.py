from django.db import models
from django.db.models.functions import Now


class Therapist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    license_type = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    tax_id = models.CharField(max_length=100)
    npi = models.CharField(max_length=10)
    street = models.CharField(max_length=100)
    apt_bldg_ste = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)
    therapist_status = models.BooleanField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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
    therapist = models.ForeignKey(Therapist, on_delete=models.PROTECT)
    diagnosis = models.CharField(max_length=100, default=None, db_default=None)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Location(models.Model):
    location_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    apt_bldg_ste = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)

    def __str__(self):
        return self.location_name


class Service(models.Model):
    cpt_code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.cpt_code


class Estimate(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    date_of_estimate = models.DateTimeField(db_default=Now())
    service = models.ManyToManyField(Service, through="EstimateServiceDetails")
    estimate_provided = models.BooleanField(db_default=True)


class EstimateServiceDetails(models.Model):
    estimate = models.ForeignKey(Estimate, on_delete=models.PROTECT)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    rate = models.IntegerField()
    quantity = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Estimate Details"
