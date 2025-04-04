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

@api_view(["GET"])
def get_product(request, id):
    try:
        data = Products.objects.get(id=id)
        serializedProductes = ProductSerializer(data).data
        return Response(serializedProductes, status=200)
    except Products.DoesNotExist:
        return Response({"message": "Product not found"}, status=404)

@api_view(["POST"])
def create_product(request):
    try:
        data = request.data
        product = ProductSerializer(data=data)
        if product.is_valid():
            product.save()
            return Response(product.data, status=201)
        return Response(product.errors, status=400)
    except Exception as e:
        return Response({"message": "Something went wrong"}, status=500)