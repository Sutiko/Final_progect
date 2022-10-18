from django.urls import path
from . import views

urlpatterns = [
    path('',views.base, name='home'),
    path('shop/',views.shop, name='shop'),
    path('<int:id>/view', views.product, name='view'),
    path('<int:id>/buy', views.buy, name='buy'),
]