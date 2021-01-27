from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
# models
from django.contrib.auth.models import User
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


# Serializers

class CampusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = '__all__'


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class ClassroomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'


class ClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class EmployeeSerializers(serializers.ModelSerializer):

    profile_image = Base64ImageField(required=False)
    department_name = serializers.CharField(
        source="department.department_name", read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'


class StudentSerializers(serializers.ModelSerializer):
    profile_image = Base64ImageField(required=False)
    department_name = serializers.CharField(
        source="school_class.department", read_only=True)

    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseStudentDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourseStudentDetail
        fields = '__all__'


class LessionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lession
        fields = '__all__'


class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class ActivationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Activation
        fields = '__all__'


class StudentAttendanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = '__all__'


class EventAttendanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = EventAttendance
        fields = '__all__'


class EmployeeTimeSheetSerializers(serializers.ModelSerializer):
    checkin_image = Base64ImageField(required=False)
    checkout_image = Base64ImageField(required=False)
    employee_first_name = serializers.CharField(
        source='employee.first_name', read_only=True)
    employee_last_name = serializers.CharField(
        source='employee.last_name', read_only=True)
    campus_name = serializers.CharField(
        source='campus.campus_name', read_only=True)

    class Meta:
        model = EmployeeTimeSheet
        fields = '__all__'


class ModelLinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = ModelLink
        fields = '__all__'


class ErrorLogSerializers(serializers.ModelSerializer):
    class Meta:
        model = ErrorLog
        fields = '__all__'
