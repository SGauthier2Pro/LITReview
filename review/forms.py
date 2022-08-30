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
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
        widgets = {
            'rating': forms.RadioSelect(attrs={'class': 'inline'}, choices=RATING_CHOICES),
        }


class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class FollowForm(forms.Form):
    followed_username = forms.CharField(empty_value="Nom d'utilisateur", required=False)


class UnfollowForm(forms.Form):
    delete_user_following = forms.BooleanField(widget=forms.HiddenInput, initial=True)



