import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter, get_default_application
import myapp.routing
django_asgi_app = get_asgi_application()
import django
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatrooms.settings')
django.setup()

application = ProtocolTypeRouter({
    'http' : django_asgi_app,
    'websocket' : AuthMiddlewareStack(URLRouter(
            myapp.routing.websocket_urlpatterns
        )
    )
})
