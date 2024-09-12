from django import template

register = template.Library()

@register.filter(name='cut_something')
def cut_something(value,arg):
  """
  This cuts out all values of "arg" from the string!
  """

  return value.replace(arg, '')
