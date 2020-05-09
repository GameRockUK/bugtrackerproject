from django.conf.urls import url, include
from .views import all_products

urlpatterns = [
    url('', all_products, name="products"),
]