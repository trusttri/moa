# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r"note/(?P<conversation_name>[A-Za-z0-9\-\_]+)/$", consumers.ConversationConsumer.as_asgi()),
]