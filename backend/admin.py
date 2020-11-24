from django.contrib import admin

# Register your models here.
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

admin.site.register(Campus) 
admin.site.register(Department) 
admin.site.register(Classroom) 
admin.site.register(Class) 
admin.site.register(Subject) 
admin.site.register(Employee) 
admin.site.register(Student) 
admin.site.register(Course) 
admin.site.register(CourseStudentDetail) 
admin.site.register(Lession) 
admin.site.register(Event) 
admin.site.register(Activation) 
admin.site.register(StudentAttendance) 
admin.site.register(EventAttendance) 
admin.site.register(EmployeeTimeSheet) 
admin.site.register(ModelLink) 
admin.site.register(ErrorLog) 
