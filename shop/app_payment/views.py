from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random


class PaymentView(APIView):
    def post(self, request, orderId):
        # TODO фронт не отправляет номер карты
        payment_number = request.data.get('number') or random.randint(10 ** 15, 10 ** 16 - 1)
        if len(str(payment_number)) == 16:
            if int(payment_number) % 2 == 0 and str(payment_number)[-1] != '0':
                data = {
                    "name": request.data.get('name'),
                    "number": payment_number,
                    "year": request.data.get('year'),
                    "month": request.data.get('month'),
                    "code": request.data.get('code'),
                }
                if 'cart' in request.session:
                    del request.session['cart']
                    request.session.modified = True
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Payment error: Card number must be even and not end with zero"},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Payment error: Card number must consist of 16 digits"},
                            status=status.HTTP_400_BAD_REQUEST)
