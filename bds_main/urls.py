from django.urls import path
from . import views  # 从当前文件夹(.)导入views


app_name = 'bds_main'
urlpatterns = [
    path('', views.bds_login, name='bds_login'),
    path('bds_main/', views.bds_main, name='bds_main'),
    path('bds_logout/', views.bds_logout, name='bds_logout')
]
