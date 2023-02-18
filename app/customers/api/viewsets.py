from rest_framework.viewsets import ModelViewSet
from customers.api.serializers import CustomerSerializer
from customers.models import Customer


class CustomerViewset(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
