from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_page(request: HttpRequest) -> HttpResponse:
    data = {
        'user': {
            'name': 'Juraqulov Azizbek',
        },
        'dashboard': {
            'total_revenue': 30_450.00
        }
    }
    return render(request=request, template_name='index.html', context=data)
    

def projects_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='projects.html')
    

def inbox_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='inbox.html')
    

def analytics_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='analytics.html')
    