from django.shortcuts import render, redirect
from .forms import ReviewForm

def review_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm()
    return render(request, 'reviews_app/review_form.html', {'form': form})