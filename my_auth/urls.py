from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.userLogin, name='userlogin'),
    path('logout/', views.userLogOut, name='userlogout'),
    path('edit_profile/', views.editUserProfile, name='editprofile'),
    path('register/', views.userRegister, name='register'),
    path('change_password/', views.changeUserPassword, name='changepassword'),
    path('change_password2/', views.changeUserPassword2, name='changepassword2'),
]