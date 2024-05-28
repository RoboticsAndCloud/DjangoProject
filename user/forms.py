from .models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):

    """
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    organization = forms.CharField(max_length=150)
    title = forms.CharField(max_length=150)
    phone_number = forms.CharField(max_length=15)
    """
    
    def __init__(self, *args, **kwargs):

        super(RegistrationForm, self).__init__(*args, **kwargs)

        # Change autofocus to first_name field
        self.fields['email'].widget.attrs['autofocus'] = 'off'
        self.fields['first_name'].widget.attrs['autofocus'] = 'on'

    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'organization', 'title', 'phone_number']