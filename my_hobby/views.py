# mysite/views.py

from django.http import HttpResponse


def index(request):
    """
    View function for the index page.
    """
    return HttpResponse('Hello world!')
