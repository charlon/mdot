from django.conf import settings
from django.template.loader import get_template
from django.template import RequestContext, Context
from django.shortcuts import render_to_response, render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .mdot_rest_client.client import MDOT
from .forms import ReviewForm

import urllib
import json
from forms import ReviewForm
from models import SponsorForm, ManagerForm, AppForm, Agreement


def home(request):
    params = {"resources": MDOT().get_resources(featured=True)}
    return render(request, "mdot/home.html", params)


def developers(request):
    return render(request, "mdot/developers/home.html")


def guidelines(request):
    params = {"ux_contact": getattr(settings, "MDOT_UX_CONTACT", None)}
    return render(request, "mdot/developers/guidelines.html", params)


def process(request):
    return render(request, "mdot/developers/process.html")


def request(request):
    if request.method == 'POST':
        sponsorForm = SponsorForm(request.POST, prefix='sponsor')
        managerForm = ManagerForm(request.POST, prefix='manager')
        appForm = AppForm(request.POST, prefix='app')
        if (sponsorForm.is_valid() and managerForm.is_valid()
                and appForm.is_valid()):
            sponsor = sponsorForm.save()
            manager = managerForm.save()
            app = appForm.save(commit=False)
            app.app_sponsor = sponsor
            app.app_manager = manager
            app.save()
            # create and save agreement model
            agreement = Agreement(
                sponsor=sponsor,
                app=app,
            )
            agreement.save()

            params = {
                'service_email': getattr(settings, 'MDOT_SERVICE_EMAIL'),
                'ux_contact': getattr(settings, 'MDOT_UX_CONTACT'),
            }
            return render_to_response(
                'mdot/developers/thanks.html',
                params)

    else:
        # use prefixes to avoid duplicate field names
        sponsorForm = SponsorForm(prefix='sponsor')
        managerForm = ManagerForm(prefix='manager')
        appForm = AppForm(prefix='app')

        forms = {
            'sponsorform': sponsorForm,
            'managerform': managerForm,
            'appform': appForm,
        }

    # return forms to review page
    return render(request, 'mdot/developers/request.html', forms)
