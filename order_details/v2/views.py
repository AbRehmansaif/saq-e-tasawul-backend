from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from order_details.models import Order, OrderDetails
from order_details.v2.serializers import OrderSerializer, OrderDetailsSerializers


@api_view(['GET', 'POST'])
def OrderView(request):
    """
    List all Orders or create a new Orders.
    """
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'POST'])
def OrderDetailsView(request):
    """
    List all Orders Details or create a new Orders Details.
    """
    if request.method == 'GET':
        orderDetail = OrderDetails.objects.all()
        serializer = OrderDetailsSerializers(orderDetail, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderDetailsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
