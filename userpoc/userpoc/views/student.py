from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from userpoc.models import Student
from userpoc.serializers import StudentModelSerializer
from django.http import HttpResponse


class StudentViewSet(GenericViewSet):

    def get_student(self, request, student_id, *args, **kwargs):
        '''
        :param request: request object
        :param student_id: student id for which the data is requested
        :param args:
        :param kwargs:
        :return: student data for student it
        '''
        student = Student.objects.get(id=student_id)
        serializer = StudentModelSerializer(student)
        serializer.is_valid()
        return Response(serializer.data, HTTP_200_OK)
