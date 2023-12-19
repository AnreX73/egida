from django.shortcuts import render


def index(request):
    context = {
        'title':'главная страница'
        
    }
    return render(request, 'core/index.html', context=context)
