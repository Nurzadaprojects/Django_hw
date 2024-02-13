from django.shortcuts import render
from django.http import HttpResponse





def test_view(requests):
    return HttpResponse('Hello it is my project!')



def main_view(request):
    return render(request, 'index.html' )