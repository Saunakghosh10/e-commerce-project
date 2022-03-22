from django import template
register = template.Library()

@register.filter
def list_item(lst, i):
    try:
        return lst[i]
    except:
        return None


@register.simple_tag
def mul(x, y):
    x = float(str(x))
    y = float(str(y))

    return x * y

@register.simple_tag
def add(x, y):
    x = float(str(x))
    y = float(str(y))

    return x + y

@register.filter
def update(value):
    data = value
    return data


