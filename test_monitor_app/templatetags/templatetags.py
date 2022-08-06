from django import template 

register = template.Library()

def get0(array):
    return array[0]

register.filter('get0', get0)

def get1(array):
    return array[1]

register.filter('get1', get1)

def length(array):
    return len(array)

register.filter('len', length)

