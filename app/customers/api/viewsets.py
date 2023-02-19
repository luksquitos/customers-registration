from rest_framework.viewsets import ModelViewSet
from customers.api.serializers import CustomerSerializer
from customers.models import Customer
from rest_framework.pagination import PageNumberPagination



class ShortPagination(PageNumberPagination):
    page_size = 10


class CustomerViewset(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    pagination_class = ShortPagination