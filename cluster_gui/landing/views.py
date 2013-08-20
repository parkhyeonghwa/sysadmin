# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):


    message = "cluster_monitoring"

    return render_to_response('test.html', {'title': message}, context_instance=RequestContext(request))



