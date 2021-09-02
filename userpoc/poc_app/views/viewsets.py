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
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        data = request.data
        # Create a user for this tenant PS: In our case
        # we will search for this user in the DB against the phone number
        u = CribUser.objects.create_user(username=data.get('mobile'), phone_no=data.get('mobile'))
        u.is_active = False
        u.save()

        # create tenant
        t = Tenant()
        t.name = data.get('name')
        t.age = data.get('age')
        t.user = u

        u.is_tenant = True
        u.is_active = True

        # search operator
        op = Operator.objects.get(user=request.user)
        t.operator = op
        t.save()

        return Response({'msg': 'data saved'}, HTTP_200_OK)

    def validate_otp(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        # validate otp in redis

        # happy case

        # create crib user in the db with
        # create token and return the token value

    def add_profile(self):
        pass

    # get CribUser for the mobile number
    # Tenant object
    # CDN =>
    #
    # create operator
    # oper.user = Crib user

    def create_otp(self):
        pass


class LoginSignupViewSet(GenericViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated & IsSpecialOperator]
    otp_handler = OtpHandler()

    def generate_otp(self, request, *args, **kwargs):
        """
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pass

        # Validate the request Data
        # validate if the user is blocked ( redis key with prefix otp_b )
        # if the otp exists in redis
        # if resend_attempt key is <=0
        # put (key: otp_b<username> , value: True) in the redis for X time ( configurable)
        # return forbidden

        # decrement resend attempts in redis
        # send otp
        # return 200

        # else
        # generate OTP
        # put otp in redis with default values (resend attempts , validation attempts, otp)
        # with redis key prefix: otp_u<username>
        # send otp
        # return 200

    def validate_otp(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        # Validate the request Data
        # validate if the user is blocked ( redis key with prefix otp_b )
        # if otp does not exist:
        # return 404

        # if the otp exists in redis
        # if validation attempt key is <=0
        # return forbidden
        # create and save CribUser
        # create and save token
        # return token

        # if otp does not match
        # decr validation attempt key in redis
        # if validation attempt <=0
        # mark blocked for X amount of time
        # return forbidden

        # return 200
