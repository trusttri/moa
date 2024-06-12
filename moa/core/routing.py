# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r"note/(?P<seed_note_id>[A-Za-z0-9\-\_]+)/$", consumers.NoteConsumer.as_asgi()),
]