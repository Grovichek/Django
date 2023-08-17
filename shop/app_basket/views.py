from app_product.models import Product
from app_product.serializers import ProductSerializer

from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.parsers import JSONParser


class BasketView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Получение идентификатора товара и количества из запроса
            product_id = request.data.get('id')
            product_count = request.data.get('count')

            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return JsonResponse({"error": "Product not found"}, status=404)

            # Инициализация корзины в сессии, если отсутствует
            if 'cart' not in request.session:
                request.session['cart'] = {}

            cart = request.session['cart']

            if str(product_id) not in cart:
                # Добавление товара в корзину, если он еще не там
                cart[str(product_id)] = {
                    "product": ProductSerializer(product).data,
                    "count": 0
                }

            # Увеличение количества товара в корзине
            cart[str(product_id)]['count'] += product_count
            request.session.modified = True

            return self.get(request)  # Возврат обновленной корзины
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def get(self, request, *args, **kwargs):
        try:
            # Получение текущей корзины из сессии
            cart = request.session.get('cart', {})
            products_in_cart = []

            # Формирование списка товаров в корзине с количеством
            for product_id, cart_item in cart.items():
                product_data = cart_item['product']
                product_data['count'] = cart_item['count']
                products_in_cart.append(product_data)

            # Возврат списка товаров в корзине в формате JSON
            return JsonResponse(products_in_cart, status=200, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    def delete(self, request, *args, **kwargs):
        try:
            data = JSONParser().parse(request)
            product_id = data.get('id')
            product_count = data.get('count', 1)

            if not product_id:
                return JsonResponse({"error": "Item ID is required"}, status=400)

            cart = request.session.get('cart', {})
            if str(product_id) in cart:
                if product_count > 1:
                    # Удаление всех товаров данного типа из корзины
                    del cart[str(product_id)]
                else:
                    # Уменьшение количества товара в корзине
                    cart[str(product_id)]['count'] -= 1
                    if cart[str(product_id)]['count'] <= 0:
                        del cart[str(product_id)]
                request.session.modified = True

            return self.get(request)  # Возврат обновленной корзины
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
