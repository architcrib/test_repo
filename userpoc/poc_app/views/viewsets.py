from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from poc_app.models import Tenant, Operator
from poc_app.serializers import OperatorModelSerializer, TenantModelSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from poc_app.permissions import IsOperator, IsTenant


class TenantViewSet(GenericViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated & IsTenant]

    def get_tenant(self, request, tenant_id, *args, **kwargs):
        '''
        :param request: request object
        :param tenant_id: tenant id for which the data is requested
        :param args:
        :param kwargs:
        :return: student data for student it
        '''

        tenant = Tenant.objects.get(user_id=tenant_id)
        serializer = TenantModelSerializer(tenant)
        return Response(serializer.data, HTTP_200_OK)


class OperatorViewSet(GenericViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated & IsOperator]

    def get_operator(self, request, operator_id, *args, **kwargs):
        '''
        :param request: request object
        :param operator_id: operator id for which the data is requested
        :param args:
        :param kwargs:
        :return: student data for student it
        '''

        operator = Operator.objects.get(user_id=operator_id)
        serializer = OperatorModelSerializer(operator)
        return Response(serializer.data, HTTP_200_OK)
