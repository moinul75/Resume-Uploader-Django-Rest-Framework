from django.urls import path
from . import views

urlpatterns = [
    path('resume',views.ProfileView.as_view(),name='profile_view'),
    path('list',views.ProfileView.as_view(),name='list')
]
