from django.shortcuts import render


def index(request):
    data = {
        'title': 'Main page!!',
        'values': ['a', '2', '3'],
        'obj': {
            'car': "BMW",
            'color': "red",
            'age': 20
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
