from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.event_index, name='event_index'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
    path('<int:pk>/map/', views.view_map, name='view_map'),
    path('create/', views.create_event, name='create_event'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search, name="search"),
    path('logout/', views.logout_request, name="logout_request"),


    path('<int:event_id>/register/', views.register, name='register'),
    path('<int:event_id>/unregister/', views.unregister, name='unregister'),
]