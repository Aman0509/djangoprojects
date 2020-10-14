from django import template

register = template.Library()


@register.filter(name='myupper')   # This is another way of registering your filter
def custupper(value):
    result = value[0:3].upper()+value[3:]
    return result

# By this way also, you can registered your filter
# register.filter('myupper', custupper)
