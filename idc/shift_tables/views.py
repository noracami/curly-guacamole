from django.shortcuts import render

from .models import Shift_table

# Create your views here.
def shitf_table_list(request):
    shift_tables = Shift_table.objects.all()
    return render(request, 'shift_tables/shitf_table_list.html',
        {'shift_tables': shift_tables}
    )
