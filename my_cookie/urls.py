from django.urls import path, include
from . import views

urlpatterns = [
    path('set_cookie/', views.set_browser_cookie),
    path('get_cookie/', views.get_browser_cookie),
    path('del_cookie/', views.del_browser_cookie)
]