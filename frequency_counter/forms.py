from .models import Web_address
from django.forms import ModelForm

class Web_addressForm(ModelForm):
    class Meta:
        model = Web_address
        fields = ['url']