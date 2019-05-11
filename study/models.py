from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 20, verbose_name="학생이름")
    shool_name = models.CharField(max_length = 20, verbose_name="학교")
    grade = models.IntegerField(verbose_name="학년")
    come_day = models.CharField(max_length=10, verbose_name="등원요일", blank=True)
    status = models.BooleanField(default=True, verbose_name="등록상태")

    def __str__(self):
        return self.name


class Course(models.Model):
    level = models.CharField(max_length=20, verbose_name="학년")
    middle_unit = models.CharField(max_length = 20, verbose_name="중단원")
    small_unit = models.CharField(max_length = 20, verbose_name="소단원")
    index = models.IntegerField(verbose_name="순번")

    def __str__(self):
        return self.small_unit

STUDY_CHOICE = (
    ( 3 , 'good' ),
    ( 2 , 'normal' ),
    ( 1 , 'bad' ),

)

class DailyNote(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="학생이름")
    study_day = models.DateField(verbose_name="날짜", blank=True)
    come_status = models.IntegerField(choices=STUDY_CHOICE, verbose_name="출결", blank=True, null=True)
    homework_complete = models.IntegerField(choices=STUDY_CHOICE, verbose_name="과제여부", blank=True, null=True)
    homework_status = models.CharField(max_length=200, blank=True, verbose_name="과제상태")
    contents = models.CharField(blank=True, max_length=200, verbose_name="학습내용")
    test1 = models.IntegerField(blank=True, verbose_name="소단원테스트점수", null=True)
    test1_content = models.CharField(max_length=200, blank=True, verbose_name="소단원테스트내용")
    test2 = models.IntegerField(blank=True, verbose_name="중단원테스트점수", null=True)
    test2_content = models.CharField(max_length=200, blank=True, verbose_name="중단원테스트내용")
    test3 = models.IntegerField(blank=True, verbose_name="대단원테스트점수", null=True)
    test3_content = models.CharField(max_length=200, blank=True, verbose_name="대단원테스트내용")
    note = models.CharField(max_length=1500, blank=True, verbose_name="비고")
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
