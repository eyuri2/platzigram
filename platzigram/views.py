""" Platzigram views """

# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime


def hello_world(request):
    """Return greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Current server time is {now}')


def hi(request):
    """Ordered list numbers"""
    numbers = request.GET['numbers'].split(',')
    numbersSorted = sorted([int(number) * 2 for number in numbers])
    return JsonResponse(numbersSorted, safe=False)


