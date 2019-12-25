from django.urls import path
from . import views

app_name = 'vehicle'
urlpatterns = [
    path('', views.VehicleListView.as_view(), name='list'),
    path('create/', views.VehicleCreateView.as_view(), name='create'),
    path('video/', views.VideoConference.as_view(), name='video'),
    path('detail/<int:pk>/', views.VehicleDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.VehicleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.VehicleDeleteView.as_view(), name='delete'),
]
