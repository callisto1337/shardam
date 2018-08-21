from django.http import JsonResponse
from django.views import View

from .forms import ReservationForm


class MakeReservation(View):

    def post(self, request, *args, **kwargs):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'OK'})

        return JsonResponse({'status': 'FAIL'})
