from django.urls import path
from . import views
urlpatterns=[
    path('login',views.login,name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('accounts/logout', views.logout, name='logout'),
    path('appointment', views.appointment,name='appointment'),
    path('aappointment', views.aappointment,name='aappointment'),
    path('python',views.python,name = 'python'),
    path('dr_one',views.dr_one,name='dr_one'),
    path('dr_two',views.dr_two,name='dr_two'),
    path('dr_three', views.dr_three, name='dr_three'),
    path('dr_four', views.dr_four, name='dr_four'),
    path('dr_five', views.dr_five, name='dr_five'),
    path('dr_six', views.dr_six, name='dr_six'),
    path('dr_seven', views.dr_seven, name='dr_seven'),
    path('dr_eight', views.dr_eight, name='dr_eight'),
    path('del_one',views.del_one,name='del_one')
]