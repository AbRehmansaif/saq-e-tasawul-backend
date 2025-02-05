from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from payment.models import Payment
from payment.v2.serializers import PaymentSerializer


@api_view(['GET', 'POST'])
def PaymentView(request):
    """
    List all categories or create a new category.
    """
    if request.method == 'GET':
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
