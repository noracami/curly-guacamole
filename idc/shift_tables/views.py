from django.shortcuts import render

from .models import Shift

# Create your views here.
def shift_list(request):
    shifts = Shift.objects.all()
    return render(request, 'shift_tables/shift_list.html',
        {'shifts': shifts}
    )
