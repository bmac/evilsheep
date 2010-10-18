# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext

import hashlib

def show_user(request, username):
    user = get_object_or_404(User, username=username)
    email = user.email.strip()
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?d=monsterid"
    return render_to_response('accounts/show_user.html', locals(), context_instance=RequestContext(request))
