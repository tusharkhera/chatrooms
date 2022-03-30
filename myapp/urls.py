from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('room/<str:group_id>/', views.index, name='index'),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('create/', views.createRoom, name='create-room'),
    path('join/', views.joinRoom, name='join-room'),
    path('signup/', views.SignUpView.as_view(), name='sign-up'),
    path('login/', views.log_in, name='log-in'),
    path('logout/', views.log_out, name='log-out'),
    path('chats/', views.chats, name='chats'),
    path('delete/', views.delete_room, name='del-grp'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)