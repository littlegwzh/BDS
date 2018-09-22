from django.shortcuts import render  # 导入重定向
from django.contrib.auth.decorators import login_required
from .models import Station


@login_required
def bds_setup(request):
    return render(request, "bds_setup/8-bds_setup.html")


@login_required
def station(request):
    station_detail = Station.objects.all()
    unique_floor = Station.objects.order_by('floor').values('floor').distinct()
    unique_area = Station.objects.order_by('area').values('area').distinct()
    unique_line = Station.objects.order_by('line').values('line').distinct()
    context = {
        'station_detail': station_detail,
        'unique_floor': unique_floor,
        'unique_area': unique_area,
        'unique_line': unique_line,
    }
    return render(request, "bds_setup/8-02-station.html", context)
