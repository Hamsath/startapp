from django.http import Http404, HttpResponse
from django.shortcuts import render
import datetime

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
