from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Products
from products.serializers import ProductSerializer


# Create your views here.
def hello(request):
    data = Products.objects.all()
    if not data:
        data = Products(name="samsung", description="samsung phone", price=1000, is_available=True)
        data.save()

    data[0].name = "iphone"
    data[0].save()

    data[0].refresh_from_db()
    # data = data.objects.all()
    print(data[0])
    return HttpResponse("Hello, World!")

@api_view(["GET"])
def get_products(request):
    data = Products.objects.all()
    serializedProductes = ProductSerializer(data, many=True).data
    return Response(serializedProductes, status=200)
