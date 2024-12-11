from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'greeting': 'Welcome to my Home Page!',
        'items': ['Item 1', 'Item 2', 'Item 3']
    }
    return render(request, 'index.html', context)