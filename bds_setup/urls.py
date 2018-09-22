from django.urls import path
from . import views  # 从当前文件夹(.)导入views


app_name = 'bds_setup'
urlpatterns = [
    path('bds_setup/', views.bds_setup, name='bds_setup'),
    path('station/', views.station, name='station'),
]
