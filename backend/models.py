from django.db import models
from datetime import date
from django.contrib.auth.models import User
import uuid

# Create your models here.


def upload_to_student_profile(instance, filename):
    extension = filename.split(".")[-1]
    return "images/students/profiles/%s/%s.%s" % (instance.student_id, uuid.uuid4(), extension)


def upload_to_student_attendance(instance, filename):
    extension = filename.split(".")[-1]
    return "images/students/attendances/%s/%s-%s.%s" % (instance.Student.student_id, date.today().strftime("%Y%m%d%H%M%S"), uuid.uuid4(), extension)


def upload_to_employee_profile(instance, filename):
    extension = filename.split(".")[-1]
    return "images/employees/profiles/%s/%s.%s" % (instance.employee_id, uuid.uuid4(), extension)


def upload_to_employee_attendance(instance, filename):
    extension = filename.split(".")[-1]
    return "images/employees/attendances/%s/%s-%s.%s" % (instance.Employee.employee_id, date.today().strftime("%Y%m%d%H%M%S"), uuid.uuid4(), extension)

# ---------------------------------------------------------------------------------------


def upload_to_train_model(instance, filename):
    extension = filename.split(".")[-1]
    return "models/trained/%s-%s-%s.%s" % (str(instance.train_model_id).zfill(4), date.today().strftime("%Y%m%d"), uuid.uuid4(), extension)


def upload_to_employee_face_model(instance, filename):
    extension = filename.split(".")[-1]
    return "models/employees/%s-%s-%s.%s" % (instance.employee_id, date.today().strftime("%Y%m%d"), uuid.uuid4(), extension)


def upload_to_student_face_model(instance, filename):
    extension = filename.split(".")[-1]
    return "models/student/%s-%s-%s.%s" % (instance.student_id, date.today().strftime("%Y%m%d"), uuid.uuid4(), extension)


def upload_to_log(instance, filename):
    extension = filename.split(".")[-1]
    return "logs/error/%s-%s-%s.%s" % (str(instance.log_id).zfill(4), date.today().strftime("%Y%m%d"), uuid.uuid4(), extension)

# ---------------------------------------------------------------------------------------


class Campus(models.Model):
    campus_id = models.CharField(max_length=1, primary_key=True)
    campus_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    max_floor = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return str(self.campus_name)


class Department(models.Model):
    department_id = models.CharField(max_length=10, primary_key=True)
    department_name = models.CharField(max_length=100)
    phone_numer = models.CharField(max_length=10, null=False, blank=True)


class Classroom(models.Model):
    classroom_id = models.CharField(max_length=10, primary_key=True)
    floor = models.IntegerField()
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)


class Class(models.Model):
    class_id = models.CharField(max_length=10, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)


class Subject(models.Model):
    subject_id = models.CharField(max_length=10, primary_key=True)
    subject_name = models.CharField(max_length=100)
    theory_credit = models.FloatField()
    practice_credit = models.FloatField()


class Employee(models.Model):
    MALE = "M"
    FEMALE = "F"
    ENABLE = 1
    DISABLE = 0
    GENDER_CHOICE = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    STATUS_CHOICE = [
        (ENABLE, 'Enable'),
        (DISABLE, 'Disable'),
    ]
    employee_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    birthday = models.DateField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    profile_image = models.ImageField(upload_to=upload_to_employee_profile)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    self_code = models.CharField(max_length=255, blank=True)
    encode = models.TextField(blank=True)
    model_url = models.URLField(blank=True)
    model_file = models.FileField(
        upload_to=upload_to_employee_face_model, blank=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICE, default=ENABLE)


class Student(models.Model):
    MALE = "M"
    FEMALE = "F"
    ENABLE = 1
    DISABLE = 0
    GENDER_CHOICE = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    STATUS_CHOICE = [
        (ENABLE, 'Enable'),
        (DISABLE, 'Disable'),
    ]
    student_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    birthday = models.DateField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    profile_image = models.ImageField(upload_to=upload_to_student_profile)
    school_class = models.ForeignKey(Class, on_delete=models.PROTECT)
    self_code = models.CharField(max_length=100, blank=True)
    encode = models.TextField(blank=True)
    model_url = models.URLField(blank=True)
    model_file = models.FileField(
        upload_to=upload_to_student_face_model, blank=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICE, default=ENABLE)


class Course(models.Model):
    ENABLE = 1
    DISABLE = 0
    STATUS_CHOICE = [
        (ENABLE, 'Enable'),
        (DISABLE, 'Disable'),
    ]
    course_id = models.CharField(max_length=10, primary_key=True)
    day_start = models.DateField()
    day_end = models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Employee, on_delete=models.PROTECT)
    term = models.CharField(max_length=10)
    status = models.IntegerField(choices=STATUS_CHOICE, default=ENABLE)


class CourseStudentDetail(models.Model):
    coursedetail_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Lession(models.Model):
    lession_id = models.CharField(max_length=10, primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    room = models.ForeignKey(Classroom, on_delete=models.PROTECT)
    check_code = models.CharField(max_length=100, blank=True)


class Event(models.Model):
    ENABLE = 1
    DISABLE = 0
    STATUS_CHOICE = [
        (ENABLE, 'Enable'),
        (DISABLE, 'Disable'),
    ]
    event_id = models.CharField(max_length=10, primary_key=True)
    event_name = models.CharField(max_length=255)
    day_start = models.DateField()
    day_end = models.DateField()
    status = models.IntegerField(choices=STATUS_CHOICE, default=ENABLE)


class Activation(models.Model):
    ENABLE = 1
    DISABLE = 0
    STATUS_CHOICE = [
        (ENABLE, 'Enable'),
        (DISABLE, 'Disable'),
    ]
    activation_id = models.CharField(max_length=10, primary_key=True)
    activation_name = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date_time_start = models.DateField()
    date_time_end = models.DateField()
    staged_area = models.CharField(max_length=255)
    status = models.IntegerField(choices=STATUS_CHOICE, default=ENABLE)
    check_code = models.CharField(max_length=100, blank=True)


class StudentAttendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lession = models.ForeignKey(Lession, on_delete=models.CASCADE)
    checkin_time = models.DateTimeField()
    checkin_image = models.ImageField(upload_to=upload_to_student_attendance)
    checkin_method = models.CharField(max_length=10)
    actual_location = models.CharField(max_length=100)


class EventAttendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    activation = models.ForeignKey(Activation, on_delete=models.CASCADE)
    checkin_time = models.DateTimeField()
    checkin_image = models.ImageField(upload_to=upload_to_student_attendance)
    checkin_method = models.CharField(max_length=10)
    actual_location = models.CharField(max_length=100)


class EmployeeTimeSheet(models.Model):
    IS_CHECKIN = 1
    IS_CHECKOUT = 2
    STATUS_CHOICE = [
        (IS_CHECKIN, 'Is Check-in'),
        (IS_CHECKOUT, 'Is Check-out'),
    ]
    attendance_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete = models.PROTECT) 
    checkin_time = models.DateTimeField(blank=True)
    checkout_time = models.DateTimeField(blank=True)
    checkin_image = models.ImageField(
        upload_to=upload_to_employee_attendance, blank=True)
    checkout_image = models.ImageField(
        upload_to=upload_to_employee_attendance, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICE, default=IS_CHECKIN)


class ModelLink(models.Model):
    train_model_id = models.AutoField(primary_key=True)
    model_url = models.URLField(blank=True)
    model_file = models.FileField(upload_to=upload_to_train_model, blank=True)
    update_date = models.DateTimeField()


class ErrorLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    user_account = models.CharField(max_length=100)
    err_title = models.CharField(max_length=100)
    user_note = models.CharField(max_length=100)
    log_file = models.FileField(upload_to=upload_to_log)
    report_time = models.DateTimeField()