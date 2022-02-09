from django.urls import path
from .consumers import *

websocket_urlpatterns = [
    path('wss/jwc/<str:group_name>/', MyJsonWebSocketConsumer.as_asgi()),
    # path('ws/ajwc/<str:group_name>/', MyAsyncJsonWebSocketConsumer.as_asgi()),
]