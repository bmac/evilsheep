from django.conf import settings
from django.contrib.auth.models import User

from registration import signals
from registration.forms import RegistrationForm

from greatape import MailChimp

class OneStepMCBackend(object):
    """
    A registration backend which follows a simple workflow:

    1. User signs up, active account is created.

    2. A mailchimp Email is sent to user so they can join our mailing list.

    Using this backend requires that

    * ``registration`` be listed in the ``INSTALLED_APPS`` setting
      (since this backend makes use of models defined in this
      application).

    Additionally, registration can be temporarily closed by adding the
    setting ``REGISTRATION_OPEN`` and setting it to
    ``False``. Omitting this setting, or setting it to ``True``, will
    be interpreted as meaning that registration is currently open and
    permitted.

    """

    mc = MailChimp(settings.MAILCHIMP_KEY)

    def register(self, request, **kwargs):
        """
        Given a username, email address and password, register a new
        user account, which will initially be active.

        After the ``User`` and ``RegistrationProfile`` are created and
        the activation email is sent, the signal
        ``registration.signals.user_registered`` will be sent, with
        the new ``User`` as the keyword argument ``user`` and the
        class of this backend as the sender.

        """
        username, email, password = kwargs['username'], kwargs['email'], kwargs['password1']

        new_user = User.objects.create_user(username, email, password)
        new_user.save()

        lists = self.mc.lists()
        self.mc.listSubscribe(
            id=lists[0]['id'],
            email_address=email,
            merge_vars={'FNAME': username},
            double_optin=False
            )        
        
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user

    def activate(self, request, activation_key):
        raise NotImplementedError()

    def registration_allowed(self, request):
        """
        Indicate whether account registration is currently permitted,
        based on the value of the setting ``REGISTRATION_OPEN``. This
        is determined as follows:

        * If ``REGISTRATION_OPEN`` is not specified in settings, or is
          set to ``True``, registration is permitted.

        * If ``REGISTRATION_OPEN`` is both specified and set to
          ``False``, registration is not permitted.
        
        """
        return getattr(settings, 'REGISTRATION_OPEN', True)

    def get_form_class(self, request):
        """
        Return the default form class used for user registration.
        
        """
        return RegistrationForm

    def post_registration_redirect(self, request, user):
        """
        Return the name of the URL to redirect to after successful
        user registration.
        
        """
        return ('registration_complete', (), {})

    def post_activation_redirect(self, request, user):
        raise NotImplementedError()
