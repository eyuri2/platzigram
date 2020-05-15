""" Platzigram views """

import json
# Utilities
from datetime import datetime

# Django
from django.http import HttpResponse


def hello_world(request):
    """Return greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Current server time is {now}')


def sort_integers(request):
    """Return a greeting."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
    )


def say_hi(request, name, age):
    """Return a greeting."""
    if age < 12:
        message = f'Sorry {name.capitalize()}, you are not allowed here.'
    else:
        message = f'Hello, {name.capitalize()}! Welcome to Platzigram.'
    
    return HttpResponse(message)
