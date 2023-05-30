from django.shortcuts import render

# Create your views here.

finches = [
    {'name': 'Finchy', 'type': 'American Goldfinch', 'color': 'yellow'},
    {'name': 'Rose', 'type': 'Black Rosy-Finch', 'color': 'gray'},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })