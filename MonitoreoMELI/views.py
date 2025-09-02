from django.shortcuts import render

def index(request):
    """Vista para la página de inicio pública"""
    return render(request, 'index.html')

def about(request):
    """Vista para página about pública"""
    return render(request, 'about.html')