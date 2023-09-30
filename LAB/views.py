from django.shortcuts import render, redirect
from .forms import AppointmentForm


# Create your views here.

def view_Home(request):
    resp = render(request, 'LAB/Home.html')
    return resp


def view_Service(request):
    resp = render(request, 'LAB/Service.html')
    return resp


def view_About(request):
    resp = render(request, 'LAB/About.html')
    return resp


def view_Testimonial(request):
    resp = render(request, 'LAB/Testimonial.html')
    return resp


def view_Contact(request):
    resp = render(request, 'LAB/Contact.html')
    return resp


def view_Contact(request):
    if request.method == 'GET':
        frm_unbound = AppointmentForm()
        d1 = {'form': frm_unbound}
        resp = render(request, 'LAB/Contact.html', context=d1)
        return resp
    elif request.method == 'POST':
        frm_bound = AppointmentForm(request.POST)
        if frm_bound.is_valid():
            frm_bound.save()
            d1 = {'msg': 'Your message has been sent. Thank you!'}
            resp = render(request, 'LAB/Contact.html', context=d1)
            return resp
        else:
            d1 = {'form': frm_bound}
            resp = render(request, 'LAB/Contact.html', context=d1)
            return resp
