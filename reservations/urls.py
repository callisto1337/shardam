from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('reservations/', csrf_exempt(views.MakeReservation.as_view()), name='make-reservation'),
]
