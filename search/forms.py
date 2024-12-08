from django.forms import ModelForm

from create_client.models import Client


class SearchClient(ModelForm):

    class Meta:
        model = Client
        fields = {"first_name", "last_name"}
