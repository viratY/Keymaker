from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import CustomerSerializer,KeyMakerSerializer,RequestSerializer,ChargeSerializer
from .models import Customer,KeyMaker,Request,Charges

# Create your views here.

class CustomerList(generics.ListCreateAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    name = 'customer-list'

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    name = 'customer-detail'

class KeyMakerList(generics.ListCreateAPIView):

    queryset = KeyMaker.objects.all()
    serializer_class = KeyMakerSerializer
    name = 'keymaker-list'


class KeyMakerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = KeyMaker.objects.all()
    serializer_class = KeyMakerSerializer
    name = 'keymaker-detail'

class RequestList(generics.ListCreateAPIView):

    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    name = 'request-list'

class RequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    name = 'request-detail'

class ChargeList(generics.ListCreateAPIView):
    queryset = Charges.objects.all()
    serializer_class = ChargeSerializer
    name = 'charges-list'

class ChargeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Charges.objects.all()
    serializer_class = ChargeSerializer
    name = 'charges-deatail'

class ApiRoot(generics.GenericAPIView):

    name = 'api-root'

    def get(self,request,*args,**kwargs):

        return Response({
            'customers':reverse(CustomerList.name,request=request),
            'keymakers': reverse(KeyMakerList.name, request=request),
            'requests': reverse(RequestList.name, request=request),
            'charges': reverse(ChargeList.name, request=request)
        })
