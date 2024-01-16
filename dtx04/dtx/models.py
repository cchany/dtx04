import datetime
from unittest.util import _MAX_LENGTH
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    id = models.BigAutoField(help_text="User ID", primary_key=True)
    login_id = models.CharField(max_length=32, unique=True, verbose_name='user 아이디')
    login_pw = models.CharField(max_length=128, verbose_name='user 비밀번호')
    
    def __str__(self):
        return f'[{self.pk}] {self.pk}' 

    def get_absolute_url(self):
        return f'/dtx04/{self.pk}/'
    
    
    
    
    
class User_consultant(models.Model):
    id = models.BigAutoField(help_text="User ID", primary_key=True)
    login_id = models.CharField(max_length=32, unique=True, verbose_name='상담사 아이디')
    login_pw = models.CharField(max_length=128, verbose_name='상담사 비밀번호')


    def get_absolute_url(self):
        return f'/dtx04/{self.pk}/'
    
    def __str__(self):
        return self.login_id
    
    

class User_Medical(models.Model):
    id = models.BigAutoField(help_text="User ID", primary_key=True)
    login_id = models.CharField(max_length=32, unique=True, verbose_name='의료진 아이디')
    login_pw = models.CharField(max_length=128, verbose_name='의료진 비밀번호')


    def get_absolute_url(self):
        return f'/dtx04/{self.pk}/'
    
    def __str__(self):
        return self.login_id
    
    
    

class Counseling(models.Model):
    id = models.BigAutoField(help_text="Counseling ID", primary_key=True)
    user = models.ForeignKey("User", related_name="counseling_user", on_delete=models.CASCADE, db_column="user_id", null=True)
    date = models.DateField()
    classification = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    
    def __str__(self):
        return f'[{self.pk}] {self.user}'
    
class Result(models.Model):
    id = models.BigAutoField(help_text="Result ID", primary_key=True)
    user = models.ForeignKey("User", related_name="result_user", on_delete=models.CASCADE, db_column="user_id", null=True)    
    date = models.DateField()
    measurement_classification = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    counseling_classification = models.CharField(max_length=10)
    normal_value = models.CharField(max_length=10)

    def __str__(self):
        return f'[{self.pk}] {self.user}'
    

class Plan(models.Model):
    id = models.BigAutoField(help_text="Plan ID", primary_key=True)
    user = models.ForeignKey("User", related_name="plan_user", on_delete=models.CASCADE, db_column="user_id", null=True)
    classification = models.CharField(max_length=10)
    date = models.DateField()
    detail = models.CharField(max_length=10)
    goal = models.CharField(max_length=10)
    plan = models.CharField(max_length=10)
    evaluation = models.CharField(max_length=10)
    
    def __str__(self):
        return f'[{self.pk}] {self.user}'