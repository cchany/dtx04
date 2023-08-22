from django.urls import path
from . import views 
from .views import Medical_Patient


urlpatterns = [
    path('', views.Login, name='Login'),
    path('Login_Medi/', views.Login_Medi, name='Login_Medi'),

    
    # 상담사용
    path('Counselor_CBT/', views.Counselor_CBT, name='Counselor_CBT'),
    path('Counselor_perform/', views.Counselor_perform, name='Counselor_perform'),
    # 의료진용
    path('Medical_Service/', views.Medical_Service, name='Medical_Service'),
    # path('Medical_Patient/', views.Medical_Patient, name='Medical_Patient'),
    path('Medical_Patient/', views.Medical_Patient, name='Medical_Patient'),

    # 관리자용
    path('Admin_page/', views.Admin_page, name='Admin_page'),
    
    path('Web_member/', views.Web_member, name='Web_member'),
    path('App_member/', views.App_member, name='App_member'),
    path('Permission/', views.Permission, name='Permission'),
    path('Region_status/', views.Region_status, name='Region_status'),


]