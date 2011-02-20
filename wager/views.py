from google.appengine.api import mail

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.conf import settings

from wager.forms import WagerForm, UserForm
from wager.models import Wager, User, Entry

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
            user = User(name=user_form.cleaned_data['name'], email=user_form.cleaned_data['email'], wager=wager)
            user.save()
            mail.send_mail(sender="Oscar Wager <oscarwager@oscarwager.net",
                           to="%s" % user.email,
                           subject="Oscar Wager - %s" % user.wager.name,
                           body="""
Hi %s,

You've signed up to be part of an awesome Oscar wager!

Choose your films wisely young Padawan and eat your greens.

Here's the link to your Oscar wager: http://%s/%s/pick/%s/

Thanks,
The Oscar Wager team""" % (user.name, user.slug, settings.ROOT_URL, user.wager.slug))
            return redirect('pick', wager_slug=wager.slug, user_slug=user.slug)
    else:
        user_form = UserForm()
    return render_to_response('wager.html', {'wager': wager, 'user_form': user_form, 'ROOT_URL': settings.ROOT_URL}, context_instance=RequestContext(request))
    
def pick(request, wager_slug, user_slug):
    wager = get_object_or_404(Wager, slug=wager_slug)
    user = get_object_or_404(User, slug=user_slug)
    entries = Entry.objects.all()
    return render_to_response('pick.html', {'wager': wager, 'user': user, 'entries': entries}, context_instance=RequestContext(request))
