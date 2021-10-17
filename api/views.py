from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Delivery, Order
from .serializers import *
from rest_framework import status
from rest_framework.generics import ListAPIView


# Create your views here.

class OrdersAndDeliveriesAPIView(APIView):
    def get(self, request):
        try:
            queryset = Order.objects.all()
            response = []
            brand = self.request.query_params.get('brand')
            if brand is not None:
                queryset = queryset.filter(brand__name=brand)
            for order in queryset:   
                data = {}   
                order_serializer = OrderSerializer(order)
                items = OrderItem.objects.filter(order=order)
                item_serializer = OrderItemSerializer(items, many=True)
                delivery = Delivery.objects.filter(order=order)
                serializer_delivery = DeliverySerializer(delivery, many=True)
                data['order'] = order_serializer.data
                data['order']['products'] = item_serializer.data
                data['order']['deliveries'] = serializer_delivery.data
                response.append(data)
            message = 'Contents returned successfully'
            if len(response) is 0:
               message = 'No orders found for that Brand'
            context = {'data': response, 'success' : True, 'message': message}
            return Response(context, status=status.HTTP_200_OK)
        except Exception as error:
            context = {'message': str(error), 'success': False}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ShippedOrdersAPIView(ListAPIView):
    serializer_class = DeliverySerializer

    def get_queryset(self):
        try:
            queryset = Delivery.objects.filter(shipped=True).order_by('-order')
            order_id = self.request.query_params.get('order_id')
            order_ref = self.request.query_params.get('order_ref')
            if order_id is not None:
                queryset = queryset.filter(order_id=order_id)
            if order_ref is not None:
                queryset = queryset.filter(order__reference=order_ref)
            return queryset
        except:
            return None
     
    def get(self, request):
        try:
           data = self.serializer_class(self.get_queryset(), many=True).data
           message = 'Contents returned successfully'
           if len(data) is 0:
               message = 'No shipped deliveries found for that Order ID/Reference'
           context = {'data' : data, 'success' : True, 'message':message}
           return Response(context, status=status.HTTP_200_OK)
        except Exception as error:
           context = {'message': str(error), 'success': False}
           return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
