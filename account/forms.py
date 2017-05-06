from django.forms import ModelForm, TextInput, CharField
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class UserUpdateForm(ModelForm):
    username = CharField(
        widget=TextInput(attrs={'readonly': 'readonly'}),
        label=_('Username')
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',)
