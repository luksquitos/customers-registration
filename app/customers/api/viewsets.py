from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.status import HTTP_422_UNPROCESSABLE_ENTITY
from customers.api.serializers import CustomerSerializer
from customers.models import Customer
from customers.utils import is_cpf_valid



class ShortPagination(PageNumberPagination):
    page_size = 10


class CustomerViewset(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    pagination_class = ShortPagination
    filter_backends = [SearchFilter]
    search_fields = ["cpf"]
    
    # These functions have been overridden to check
    # the cpf coming from the POST and PUT methods.
    
    def create(self, request, *args, **kwargs):
        cpf = request.data.get('cpf')
        
        if is_cpf_valid(cpf) or not cpf:
            return super().create(request, *args, **kwargs)
        
        else:
            msg = {"msg": f"CPF '{cpf}' inválido"}
            return Response(msg, status=HTTP_422_UNPROCESSABLE_ENTITY)
        
    
    def update(self, request, *args, **kwargs):
        cpf = request.data.get('cpf')
        
        if is_cpf_valid(cpf) or not cpf:
            return super().update(request, *args, **kwargs)
        
        else:
            msg = {"msg": f"CPF '{cpf}' inválido"}
            return Response(msg, status=HTTP_422_UNPROCESSABLE_ENTITY)
