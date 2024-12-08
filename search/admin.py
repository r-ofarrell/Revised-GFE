from django.contrib import admin

from .models import Therapist, Service, Location, Estimate, EstimateDetails

admin.site.register(Therapist)
admin.site.register(Service)
admin.site.register(Location)
admin.site.register(Estimate)
admin.site.register(EstimateDetails)
