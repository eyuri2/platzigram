""" Posts views """

# Utilities
from datetime import datetime

# Django
from django.shortcuts import render

posts = [
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600/?image=1036'
    },
    {
        'title': 'Vía Lactea',
        'user': {
            'name': 'Miguel Yurivilca',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903'
    },
    {
        'title': 'New room',
        'user': {
            'name': 'Emerson Yurivilca',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076'
    },
]


def list_posts(request):
    """List existing posts"""
    return render(request, 'posts/feed.html', {'posts': posts})
