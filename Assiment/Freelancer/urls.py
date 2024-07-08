from django.urls import path,include
from . import views
urlpatterns = [
    path('proposal/<int:pk>/', views.ProsalAPIView.as_view(),name='proposal'),
]