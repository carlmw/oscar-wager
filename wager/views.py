from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from wager.forms import WagerForm

def index(request):
    wager_form = WagerForm()
    return render_to_response('index.html', {'wager_form': wager_form}, context_instance=RequestContext(request))