from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from wager.forms import WagerForm, UserForm
from wager.models import Wager, User

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
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.wager = wager
            user.save()
            return redirect('pick', slug=wager.slug)
    else:
        user_form = UserForm()
    return render_to_response('wager.html', {'wager': wager, 'user_form': user_form}, context_instance=RequestContext(request))
    
def pick(request, slug):
    wager = get_object_or_404(Wager, slug=slug)
    return render_to_response('pick.html', {'wager': wager}, context_instance=RequestContext(request))