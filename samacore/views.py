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
    print "index"
    return render(request, 'samacore/index.html', context)

def section(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    param_1 = 2
    context = {'params': param_1}
    #return render(request, 'core/section.html', context)
    #return render(request, 'core/section.html')
    #return render_to_response('samacore/section.html', response, context_instance=RequestContext(request))
    print "ici"
    return render(request, 'samacore/section.html', context)
