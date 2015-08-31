# Std libraries
from django import template

register = template.Library()

PORTFOLIO_DEFAULT_COLORS = (
    'green',
    'red',
)

@register.filter()
def colorize_percentage(value):

    
    print type(value)
    if value >= 0:
        return PORTFOLIO_DEFAULT_COLORS[0]

