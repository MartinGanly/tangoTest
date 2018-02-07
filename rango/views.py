from django.shortcuts import render

from django.http import HttpResponse

def index(request):
        context_dict = { 'boldmessage' : "Crunch, Munch, Lunch?"}
        return render(request, 'rango/index.html', context=context_dict)

def about(request):
        return HttpResponse("Here is the about page <a href='/'>Index</a>")
