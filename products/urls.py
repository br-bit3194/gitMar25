
from products import views
from django.urls import path
urlpatterns = [
    path("hello/", views.hello),
    path("allproducts/", views.get_products),
    path("product/<int:id>/", views.get_product),
    path("createproduct/", views.create_product),
]