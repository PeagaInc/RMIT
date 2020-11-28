from rest_framework import viewsets, permissions


from api.serializers import CampusSerializers
from api.serializers import DepartmentSerializers
from api.serializers import ClassroomSerializers
from api.serializers import ClassSerializers
from api.serializers import SubjectSerializers
from api.serializers import EmployeeSerializers
from api.serializers import StudentSerializers
from api.serializers import CourseSerializers
from api.serializers import CourseStudentDetailSerializers
from api.serializers import LessionSerializers
from api.serializers import EventSerializers
from api.serializers import ActivationSerializers
from api.serializers import StudentAttendanceSerializers
from api.serializers import EventAttendanceSerializers
from api.serializers import EmployeeTimeSheetSerializers
from api.serializers import ModelLinkSerializers
from api.serializers import ErrorLogSerializers

from backend.models import Campus
from backend.models import Department
from backend.models import Classroom
from backend.models import Class
from backend.models import Subject
from backend.models import Employee
from backend.models import Student
from backend.models import Course
from backend.models import CourseStudentDetail
from backend.models import Lession
from backend.models import Event
from backend.models import Activation
from backend.models import StudentAttendance
from backend.models import EventAttendance
from backend.models import EmployeeTimeSheet
from backend.models import ModelLink
from backend.models import ErrorLog


class CampusViewSet(viewsets.ModelViewSet):
    queryset = Campus.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CampusSerializers


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DepartmentSerializers


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClassroomSerializers


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClassSerializers


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubjectSerializers


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EmployeeSerializers


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentSerializers


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CourseSerializers


class CourseStudentDetailViewSet(viewsets.ModelViewSet):
    queryset = CourseStudentDetail.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CourseStudentDetailSerializers


class LessionViewSet(viewsets.ModelViewSet):
    queryset = Lession.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LessionSerializers


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EventSerializers


class ActivationViewSet(viewsets.ModelViewSet):
    queryset = Activation.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ActivationSerializers


class StudentAttendanceViewSet(viewsets.ModelViewSet):
    queryset = StudentAttendance.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentSerializers


class EventAttendanceViewSet(viewsets.ModelViewSet):
    queryset = EventAttendance.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EventAttendanceSerializers


class EmployeeTimeSheetViewSet(viewsets.ModelViewSet):
    queryset = EmployeeTimeSheet.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EmployeeTimeSheetSerializers


class ModelLinkViewSet(viewsets.ModelViewSet):
    queryset = ModelLink.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ModelLinkSerializers


class ErrorLogViewSet(viewsets.ModelViewSet):
    queryset = ErrorLog.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ErrorLogSerializers
