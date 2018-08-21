from django.shortcuts import render

from .models import Address, Social, Event


def main(request):
    addresses = Address.objects.all()
    social = Social.objects.all()

    return render(request, 'landing/index.html', {
        'addresses': addresses,
        'social': social,

        'corporate_parties': serialize_event(Event.objects.get(slug='corporate_parties')),
        'weddings': serialize_event(Event.objects.get(slug='weddings')),
        'children_event': serialize_event(Event.objects.get(slug='children')),
    })


def serialize_event(event):
    return {
        'title': event.title,
        'images': event.images.all(),
        'menu_list': event.menu_set.all(),
    }
