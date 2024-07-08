from django.urls import path,include
from . import views
urlpatterns = [
    path('register/', views.UserRegistrationAPIView.as_view(),name='register'),
    path('login/', views.UserLoginAPIView.as_view(),name='login'),
    path('logout/', views.UserLogoutAPIView.as_view(),name='logout'),
    path('active/<uid64>/<token>/',views.activate , name ="activate")
]