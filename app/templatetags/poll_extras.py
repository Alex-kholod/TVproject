from django import template

register = template.Library()


@register.simple_tag
def parse_data(key_value, item):
    item_value = item[key_value]
    return item_value
