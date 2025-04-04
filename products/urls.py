
from products import views
from django.urls import path
urlpatterns = [
    path("hello/", views.hello),
    path("products/", views.get_products),
]