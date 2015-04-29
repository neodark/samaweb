from django.shortcuts import render

from django.template import loader, RequestContext

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.

#from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    param_1 = 2
    context = {'params': param_1}
    return render(request, 'samacore/index.html', context)

def section(request):
    param_1 = 2
    context = {'params': param_1}
    return render(request, 'samacore/section.html', context)

def courses(request):
    param_1 = 2
    context = {'params': param_1}
    return render(request, 'samacore/courses.html', context)

def faq(request):
    param_1 = 2
    context = {'params': param_1}
    return render(request, 'samacore/faq.html', context)
