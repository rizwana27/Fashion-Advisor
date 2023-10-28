"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',)

def bodyshape_view(request):
    return render(request, 'app/bodyshape.html')

def skintype_view(request):
    return render(request, 'app/skintype.html')

    
