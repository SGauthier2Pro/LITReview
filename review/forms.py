from django import forms
from django.utils.safestring import mark_safe

from . import models


RATING_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 2),
    ('4', 4),
    ('5', 5)
)


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']
        widgets = {
            'rating': forms.RadioSelect(attrs={'class': 'inline'}, choices=RATING_CHOICES),
        }

