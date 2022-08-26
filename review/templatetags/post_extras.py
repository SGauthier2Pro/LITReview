from django import template
import locale

register = template.Library()


@register.filter
def model_type(value):
    return type(value).__name__


@register.simple_tag(takes_context=True)
def get_poster_display(context, user):
    if context['user'] == user:
        return 'vous avez'
    return f'{user.username} a'


@register.filter
def get_posted_at_display(posted_at):
    locale.setlocale(locale.LC_ALL, 'fr_FR')
    return f'{posted_at.strftime("%Hh%M, %d %b %Y")}'
