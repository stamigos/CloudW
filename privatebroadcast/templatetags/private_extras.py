from django import template

register = template.Library()


@register.filter
def next_to_look(d, key):
    return d[key]