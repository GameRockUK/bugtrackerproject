from django.conf.urls import url
from .views import all_products

urlpatterns = [
    url('', all_products, name="products"),
]
