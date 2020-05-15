""" Posts views """

# Utilities
from datetime import datetime

# Django 
from django.http import HttpResponse

posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yésica Cortés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'name': 'Via Láctea',
        'user': 'M. Yuri',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1066'
    },
    {
        'name': 'New room',
        'user': 'E. Yuri',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1056'
    },
]


def list_posts(request):
    """List existing posts"""
    content = []
    for post in posts:
        content.append("""
            <p><ztrong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))
