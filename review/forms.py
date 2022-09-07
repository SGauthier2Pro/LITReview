from django import forms
from django.utils.safestring import mark_safe

from . import models


RATING_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5)
)


class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix

    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
        widgets = {
            'rating': forms.RadioSelect(choices=RATING_CHOICES),
        }


class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class FollowForm(forms.Form):
    followed_username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'placeholder': "Nom d'utilisateur",
                   'size': '100%',
                   'class': 'align-self-center'
                   }
        )
    )


class UnfollowForm(forms.Form):
    delete_user_following = forms.BooleanField(widget=forms.HiddenInput, initial=True)



