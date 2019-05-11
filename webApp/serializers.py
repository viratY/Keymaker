from rest_framework import serializers
from .models import Customer,KeyMaker,Request,Charges

class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    CustomerRequests =serializers.HyperlinkedRelatedField(
                        many =True,
                        read_only=True,
                        view_name = 'request-detail'
                        )

    class Meta:
        model=Customer
        fields = (
            'url',
            'pk',
            'fname',
            'lname',
            'phoneNumber',
            'CustomerRequests'
        )


class KeyMakerSerializer(serializers.HyperlinkedModelSerializer):

    KeymakerRequests = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='request-detail'
    )

    class Meta:
        model = KeyMaker
        fields = (
            'url',
            'pk',
            'fname',
            'lname',
            'phoneNumber',
            'KeymakerRequests'
        )

class RequestSerializer(serializers.ModelSerializer):

    # The following names should be same as the model
    keymaker = serializers.SlugRelatedField(queryset=KeyMaker.objects.all(),slug_field='fname')
    customer = serializers.SlugRelatedField(queryset=Customer.objects.all(), slug_field='fname')

    class Meta:
        model = Request
        fields = (
            'url',
            'pk',
            'location',
            'dateTime',
            'keymaker',
            'customer'
        )

class ChargeSerializer(serializers.HyperlinkedModelSerializer):

    requests =  RequestSerializer()

    class Meta:

        model = Charges

        fields = (
            'url',
            'pk',
            'requests',
            'charge',
            'paid'
        )


