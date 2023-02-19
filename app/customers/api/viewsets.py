from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from customers.api.serializers import CustomerSerializer
from customers.models import Customer



class ShortPagination(PageNumberPagination):
    page_size = 10


class CustomerViewset(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    pagination_class = ShortPagination
    filter_backends = [SearchFilter]
    search_fields = ["cpf"]