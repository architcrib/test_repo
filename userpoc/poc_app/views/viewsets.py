from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from poc_app.models import Tenant, Operator, CribUser
from poc_app.serializers import OperatorModelSerializer, TenantModelSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from poc_app.permissions import IsOperator, IsTenant, IsSpecialOperator


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


class SpecialOperatorViewSet(GenericViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated & IsSpecialOperator]

    def add_tenant(self, request, *args, **kwargs):
        '''
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''

        data = request.data
        # Create a user for this tenant PS: In our case
        # we will search for this user in the DB against the phone number
        u = CribUser.objects.create_user(username=data.get('mobile'), phone_no=data.get('mobile'))
        u.save()

        # create tenant
        t = Tenant()
        t.name = data.get('name')
        t.age = data.get('age')
        t.user = u

        # search operator
        op = Operator.objects.get(user=request.user)
        t.operator = op
        t.save()

        return Response({'msg': 'data saved'}, HTTP_200_OK)