from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime

from startapp.forms import ContactForm
from django.core.mail import send_mail, get_connection

def hello(request):
    return HttpResponse("Hello world")

def current_dateTime(request):
    now = datetime.datetime.now()
    return render(request,'current_dateTime.html',{'current_date':now})

def hours_ahead(request, offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(offset)

    html = "<html> <body> In %s hour(s), it will be %s. </body></html>" %(offset, dt)

    return HttpResponse(html)

def ua_display_good1(request):
    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = 'unknown'
    return HttpResponse("Your browser is %s" % ua)

def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm( initial={'subject':'I love your site!'} )

    return render(request,'contact_form.html',{'form':form})

def thanks(request):
    return render(request,'contact_form.html',{'form':form})
