from django.urls import path,include
from . import views
urlpatterns = [
    path('list/', views.JobListAPIView.as_view(),name='add_post'),
    path('<int:pk>/', views.JobDetailsAPIView.as_view(),name='job_detils'),
    path('reveiw/<int:pk>/', views.ReveiwListAPIView.as_view(),name='reveiw'),
    path('reveiw/', views.AllReveiwListAPIView.as_view(),name='all_reveiw'),
]