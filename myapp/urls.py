from django.urls import path
from .import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('profile/',views.profile,name='profile'),
    path('register/',views.register,name='register'),
    path('otp/',views.otp,name='otp'),
    path('',views.signin,name='sign-in'),
    path('emergency-contact/',views.emergency_contact,name='emergencycontact'),
    path('logout/',views.logout,name='logout'),
]
