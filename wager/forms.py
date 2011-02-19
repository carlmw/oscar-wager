from django.forms import ModelForm

from wager.models import Wager, User

class WagerForm(ModelForm):
    class Meta:
        model = Wager
        fields = ('name',)
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email',)