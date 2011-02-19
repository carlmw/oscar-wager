from django.forms import ModelForm

from wager.models import Wager

class WagerForm(ModelForm):
    class Meta:
        model = Wager