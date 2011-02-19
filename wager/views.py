from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from wager.forms import WagerForm
from wager.models import Wager

def index(request):
    if request.method == 'POST':
        wager_form = WagerForm(data=request.POST)
        if wager_form.is_valid():
            wager = wager_form.save()
            return redirect('wager', slug=wager.slug)
    else:
        wager_form = WagerForm()
    return render_to_response('index.html', {'wager_form': wager_form}, context_instance=RequestContext(request))
    
def wager(request, slug):
    wager = get_object_or_404(Wager, slug=slug)
    return render_to_response('wager.html', {'wager': wager}, context_instance=RequestContext(request))