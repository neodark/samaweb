from django.shortcuts import render

from django.template import loader, RequestContext

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, Http404
from django.core import exceptions
from django.conf import settings
from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView
from samacore.models import Course, Participant
import simplejson as json
# Create your views here.

#from django.http import HttpResponse
courseprice = {
        'UPE': 90,
        'BLS-AED': 90,
        'Sauveteurs': 130,
        'IAS1': 150,
        'IAS2': 150,
        'Samaritains': 150
        }


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
    if request.user.is_anonymous:
        return render(request, 'samacore/courses.html', context)
    else:
        return render(request, 'samacore/courses_admin.html', context)

def faq(request):
    param_1 = 2
    context = {'params': param_1}
    return render(request, 'samacore/faq.html', context)

def membres(request):
    param_1 = 2
    context = {'params': param_1}
    if request.user.is_anonymous:
        return render(request, 'samacore/section_program_section.html', context)
    else:
        return render(request, 'samacore/section_program_section_admin.html', context)

def add_program(request):
    if request.user.is_anonymous:
        raise exceptions.PermissionDenied
    else:
        context = {}

        return render(request, 'samacore/section_program_add.html', context)

def edit_program(request):
    if request.user.is_anonymous:
        raise exceptions.PermissionDenied
    else:
        if 'sectionid' in request.GET:
            sectionid = request.GET['sectionid']

        context = {'sectionid': sectionid}

        return render(request, 'samacore/section_program_edit.html', context)


def course(request):
    coursetype = ''
    coursestatus = ''
    if 'coursetype' in request.GET:
        coursetype = request.GET['coursetype']

    if 'coursestatus' in request.GET:
        coursestatus = request.GET['coursestatus']

    context = {'coursetype': coursetype,
               'courseprice': courseprice[coursetype],
               'coursestatus': coursestatus}
    if request.user.is_anonymous:
        return render(request, 'samacore/course.html', context)
    else:
        return render(request, 'samacore/course_admin.html', context)

def add_course(request):
    if request.user.is_anonymous:
        raise exceptions.PermissionDenied
    else:
        coursetype = ''
        if 'coursetype' in request.GET:
            coursetype = request.GET['coursetype']

        context = {'coursetype': coursetype,
                   'courseprice': courseprice[coursetype]}

        return render(request, 'samacore/course_add.html', context)

def edit_course(request):
    if request.user.is_anonymous:
        raise exceptions.PermissionDenied
    else:
        coursetype = ''
        if 'coursetype' in request.GET:
            coursetype = request.GET['coursetype']

        if 'courseid' in request.GET:
            courseid = request.GET['courseid']

        context = {'coursetype': coursetype,
                   'courseprice': courseprice[coursetype],
                   'courseid': courseid}

        return render(request, 'samacore/course_edit.html', context)

def archive_course(request):
    if request.user.is_anonymous:
        raise exceptions.PermissionDenied
    else:
        coursetype = ''
        if 'coursetype' in request.GET:
            coursetype = request.GET['coursetype']

        if 'courseid' in request.GET:
            courseid = request.GET['courseid']

        context = {'coursetype': coursetype,
                   'courseprice': courseprice[coursetype],
                   'courseid': courseid}

        return render(request, 'samacore/course_archive.html', context)

def participants_course(request):
    if request.user.is_anonymous:
        raise exceptions.PermissionDenied
    else:
        coursetype = ''
        if 'coursetype' in request.GET:
            coursetype = request.GET['coursetype']

        if 'courseid' in request.GET:
            courseid = request.GET['courseid']

        context = {'coursetype': coursetype,
                   'courseid': courseid}

        return render(request, 'samacore/course_participants.html', context)

def participant_course_edit(request):
    if request.user.is_anonymous:
        raise exceptions.PermissionDenied
    else:
        coursetype = ''
        courseid = ''
        coursedates = ''
        coursetime = ''
        courselocation = ''
        participantid = ''
        if 'coursetype' in request.GET:
            coursetype = request.GET['coursetype']
        if 'courseid' in request.GEt:
            courseid = request.GET['courseid']
            course = Course.objects.get(id=courseid)
            courseinformation = course.additional_information
            jsoncourse = json.loads(courseinformation)
            coursedates     = jsoncourse['dates']
            coursetime      = jsoncourse['time']
            courselocation  = jsoncourse['location']
        if 'participantid' in request.GET:
            participantid = request.GET['participantid']
            participant = Participant.objects.get(id=participantid)

        context = {'coursetype': coursetype,
                   'courseprice': courseprice[coursetype],
                   'courseid': courseid,
                   'coursedates': coursedates,
                   'coursetime': coursetime,
                   'courselocation': courselocation,
                   'participantid': participantid,
                   'participant': participant}
        return render(request, 'samacore/participant_course.html', context)

def participant_course_delete(request):
    if request.user.is_anonymous:
        raise exceptions.PermissionDenied
    else:
        coursetype = ''
        courseid = ''
        coursedates = ''
        coursetime = ''
        courselocation = ''
        participantid = ''
        if 'coursetype' in request.GET:
            coursetype = request.GET['coursetype']
        if 'courseid' in request.GET:
            courseid = request.GET['courseid']
            course = Course.objects.get(id=courseid)
            courseinformation = course.additional_information
            jsoncourse = json.loads(courseinformation)
            coursedates     = jsoncourse['dates']
            coursetime      = jsoncourse['time']
            courselocation  = jsoncourse['location']
        if 'participantid' in request.GET:
            participantid = request.GET['participantid']
            participant = Participant.objects.get(id=participantid)

        context = {'coursetype': coursetype,
                   'courseprice': courseprice[coursetype],
                   'courseid': courseid,
                   'coursedates': coursedates,
                   'coursetime': coursetime,
                   'courselocation': courselocation,
                   'participantid': participantid,
                   'participant': participant}
        return render(request, 'samacore/course_participant_delete.html', context)


def admin_login(request):
    param_1 = 2
    context = {'params': param_1}
    return render(request, 'samacore/admin_login.html', context)

def register_course(request):
    coursetype = ''
    courseid = ''
    coursedates = ''
    coursetime = ''
    courselocation = ''
    if 'coursetype' in request.GET:
        coursetype = request.GET['coursetype']
    if 'courseid' in request.GET:
        courseid = request.GET['courseid']
        course = Course.objects.get(id=courseid)
        courseinformation = course.additional_information
        jsoncourse = json.loads(courseinformation)
        coursedates     = jsoncourse['dates']
        coursetime      = jsoncourse['time']
        courselocation  = jsoncourse['location']


    context = {'coursetype': coursetype,
               'courseprice': courseprice[coursetype],
               'courseid': courseid,
               'coursedates': coursedates,
               'coursetime': coursetime,
               'courselocation': courselocation}
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
