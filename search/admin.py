from django.contrib import admin

from .models import (
    Client,
    Therapist,
    Service,
    Location,
    Estimate,
    EstimateServiceDetails,
)

admin.site.register(Client)
admin.site.register(Therapist)
admin.site.register(Service)
admin.site.register(Location)
admin.site.register(Estimate)
admin.site.register(EstimateServiceDetails)
