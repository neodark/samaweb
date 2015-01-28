from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    param_1 = 2
    context = {'params': param_1}
    return render(request, 'core/index.html', context)


