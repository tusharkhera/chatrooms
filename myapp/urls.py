from django.urls import path
from . import views

urlpatterns = [
    path('room/<str:group_id>/', views.index, name='index'),
    path('', views.home, name='home'),
    path('create/', views.createRoom, name='create-room'),
    path('join/', views.joinRoom, name='join-room'),
    path('signup/', views.SignUpView.as_view(), name='sign-up'),
    path('login/', views.log_in, name='log-in'),
    path('logout/', views.log_out, name='log-out'),
]