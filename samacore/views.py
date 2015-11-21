from django.shortcuts import render

from django.template import loader, RequestContext

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404

from django.views.generic import TemplateView
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
    if request.user.is_anonymous():
        return render(request, 'samacore/courses.html', context)
    else:
        return render(request, 'samacore/courses_admin.html', context)

def faq(request):
    param_1 = 2
    context = {'params': param_1}
    return render(request, 'samacore/faq.html', context)

def course(request):
    coursetype = ''
    if request.GET.has_key('coursetype'):
        coursetype = request.GET['coursetype']

    context = {'coursetype': coursetype}
    if request.user.is_anonymous():
        return render(request, 'samacore/course.html', context)
    else:
        return render(request, 'samacore/course_admin.html', context)

def admin_login(request):
    param_1 = 2
    context = {'params': param_1}
    return render(request, 'samacore/admin_login.html', context)

def register_course(request):
    coursetype = ''
    courseid = ''
    if request.GET.has_key('coursetype'):
        coursetype = request.GET['coursetype']
    if request.GET.has_key('courseid'):
        courseid = request.GET['courseid']

    context = {'coursetype': coursetype,
               'courseid': courseid}
    return render(request, 'samacore/register_course.html', context)

#------------------------------------------------


class PartialGroupView(TemplateView):
    def get_template_names(self):
        if 'template_name' in self.kwargs:
            self.template_name = 'samacore/partials/' + self.kwargs.get('template_name')
        return super(PartialGroupView, self).get_template_names()

    def get_context_data(self, **kwargs):
        context = super(PartialGroupView, self).get_context_data(**kwargs)
        return context


#------------------------------------------------
