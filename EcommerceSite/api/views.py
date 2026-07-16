from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Products
from .serializers import ProductsSerilize

class ProductsViews(APIView):
    def get(self,request):
        items=Products.objects.all()
        
        serializer=ProductsSerilize(items,many=True)
        return Response(serializer.data)