from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

from django import forms


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'size': '70%', 'placeholder': "Nom d'utilisateur"})
        self.fields['username'].label = ''
        self.fields['password1'].widget.attrs.update({'size': '70%', 'placeholder': 'Mot de passe'})
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].widget.attrs.update({'size': '70%', 'placeholder': 'Confirmer mot de passe'})
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ''

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2')
        help_texts = {
            'username': None,
        }


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['password'].label = ''

    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'class': 'container-fluid text-center',
                'size': '70%',
                'placeholder': "Nom d'utilisateur"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'container-fluid text-center',
                'size': '70%',
                'placeholder': "Mot de passe"
            }
        )
    )
