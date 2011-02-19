from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from wager.forms import WagerForm
from wager.models import Wager

def index(request):
    if request.method == 'POST':
        wager_form = WagerForm(data=request.POST)
        if wager_form.is_valid():
            wager_form.save()
    else:
        wager_form = WagerForm()
    return render_to_response('index.html', {'wager_form': wager_form}, context_instance=RequestContext(request))