from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import sublocation_choices, location_choices, subcounty_choices

from .models import Entry


def index(request):
    entries = Entry.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(entries, 6)
    page = request.GET.get('page')
    paged_entries = paginator.get_page(page)

    context = {
        'entries': paged_entries
    }

    return render(request, 'entries/entries.html', context)


def entry(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)

    context = {
        'entry': entry
    }

    return render(request, 'entries/entry.html', context)


def search(request):
    queryset_list = Entry.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'weight' in request.GET:
        weight = request.GET['weight']
        if weight:
            queryset_list = queryset_list.filter(weight__lte=weight)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'subcounty_choices': subcounty_choices,
        'location_choices': location_choices,
        'sublocation_choices': sublocation_choices,
        'products': queryset_list,
        'values': request.GET
    }

    return render(request, 'entries/search.html', context)
