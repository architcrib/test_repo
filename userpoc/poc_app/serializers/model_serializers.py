from poc_app.models import *
from rest_framework import serializers

class OperatorModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operator
        fields = '__all__'


class TenantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = '__all__'# ('name', 'age')

