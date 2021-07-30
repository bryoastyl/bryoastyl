from django.shortcuts import render
from django.http import HttpResponse
from entries.choices import sublocation_choices, location_choices, subcounty_choices

from entries.models import Entry
from caters.models import Cater


def index(request):
    entries = Entry.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'entries': entries,
        'subcounty_choices': subcounty_choices,
        'location_choices': location_choices,
        'sublocation_choices': sublocation_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all caterers
    caters = Cater.objects.order_by('-hire_date')

    # Get MVP
    mvp_caters = Cater.objects.all().filter(is_mvp=True)

    context = {
        'caters': caters,
        'mvp_caters': mvp_caters
    }

    return render(request, 'pages/about.html', context)
