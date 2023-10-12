"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
# custom import

from .models import EnteredText

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


#new view added by PavanY


def text_entry_view(request):
    entered_text = None
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        entered_text_value = request.POST.get('text_input', '')

        # Create a new EnteredText object and save it to the database
        entered_text = EnteredText(text=entered_text_value)
        entered_text.save()

    # Fetch all previously stored EnteredText objects from the database
    all_entered_texts = EnteredText.objects.all()

    return render(request, 'app/input_page.html', {'entered_text': entered_text, 'all_entered_texts': all_entered_texts})

