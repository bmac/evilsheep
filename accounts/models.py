import threading

from django.conf import settings
from django.db import models

from registration.signals import user_registered

from greatape import MailChimp, MailChimpError

import logging
logger = logging.getLogger(__name__)

mc = MailChimp(settings.MAILCHIMP_KEY)

# Lets send emails asyncronously 
# http://www.chrisdpratt.com/2008/02/16/signals-in-django-stuff-thats-not-documented-well/
class SubscribeEmailThread(threading.Thread):
    def __init__(self, user, mc=None):
        self.user = user

        if mc is not None:
            self.mc = mc
        else:
            mc = MailChimp(settings.MAILCHIMP_KEY)
        threading.Thread.__init__(self)

    def run(self):
        # The actual code we want to run in the tread
        print 'username ', self.user.username
        try: 
            lists = self.mc.lists()
            mc.listSubscribe(
                id=lists[0]['id'],
                email_address=self.user.email,
                merge_vars={'FNAME': self.user.username},
                double_optin=False
                )
        except MailChimpError, e:
            print e.msg
            logger.error(e.msg)

# Signal which starts the subscribe thread
def add_to_mailinglist(sender, user, request, **kwargs):
    SubscribeEmailThread(user, mc).start()


# Create your models here.


user_registered.connect(add_to_mailinglist)
