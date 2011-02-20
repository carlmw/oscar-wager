from django.forms import ModelForm

from wager.models import Wager, User, Pick

class WagerForm(ModelForm):
    class Meta:
        model = Wager
        fields = ('name', 'description',)
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email',)
        
class PickForm(ModelForm):
    class Meta:
        model = Pick