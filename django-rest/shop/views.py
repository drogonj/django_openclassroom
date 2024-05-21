
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from shop.models import Category, Product
from shop.serializers import CategorySerializer, ProductSerializer

# class CategoryAPIView(APIView):
#     def get(self, *args, **kwargs):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True) # "many=True" indique au Serializer qu'il va recevoir un element iterable
#         return Response(serializer.data)
#
# class ProductAPIView(APIView):
#     def get(self, *args, **kwargs):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

# Replaced by following funcs to use DRF's routers

class CategoryViewSet(ReadOnlyModelViewSet): #We can inherit ModelViewSet but we do ReadOnlyModelViewSet to restrict permissions
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.filter(active=True)

class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    def get_queryset(self):
        queryset = Product.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset #We can select only product from a given category_id, example: 127.0.0.1/api/product/?category_id=1
