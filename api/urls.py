from rest_framework import routers
from django.urls import path, include
# Viewset
from api.viewsets import CampusViewSet
from api.viewsets import DepartmentViewSet
from api.viewsets import ClassroomViewSet
from api.viewsets import ClassViewSet
from api.viewsets import SubjectViewSet
from api.viewsets import EmployeeViewSet
from api.viewsets import StudentViewSet
from api.viewsets import CourseViewSet
from api.viewsets import CourseStudentDetailViewSet
from api.viewsets import LessionViewSet
from api.viewsets import EventViewSet
from api.viewsets import ActivationViewSet
from api.viewsets import StudentAttendanceViewSet
from api.viewsets import EventAttendanceViewSet
from api.viewsets import EmployeeTimeSheetViewSet
from api.viewsets import ModelLinkViewSet
from api.viewsets import ErrorLogViewSet

# Routers for API test - Using Django Rest ViewSet
router = routers.DefaultRouter()
router.register('campusses', CampusViewSet)
router.register('departments', DepartmentViewSet)
router.register('classrooms', ClassroomViewSet)
router.register('classes', ClassViewSet)
router.register('subjects', SubjectViewSet)
router.register('employees', EmployeeViewSet)
router.register('students', StudentViewSet)
router.register('courses', CourseViewSet)
router.register('coursestudentdetails', CourseStudentDetailViewSet)
router.register('lessions', LessionViewSet)
router.register('events', EventViewSet)
router.register('activations', ActivationViewSet)
router.register('studentattendances', StudentAttendanceViewSet)
router.register('eventattendances', EventAttendanceViewSet)
router.register('employeetimesheets', EmployeeTimeSheetViewSet)
router.register('modellinks', ModelLinkViewSet)
router.register('errorlogs', ErrorLogViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
