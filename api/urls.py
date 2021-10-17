from django.urls import path

from api import views

urlpatterns = [
    path('orders', views.OrdersAndDeliveriesAPIView.as_view(), name='orders'),
    path('deliveries', views.ShippedOrdersAPIView.as_view(), name='deliveries'),
]
