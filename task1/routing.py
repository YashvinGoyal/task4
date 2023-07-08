from django.urls import re_path
from home import consumers

# URLs that handle the WebSocket connection are placed here.
ws_pattern = [
    re_path(r'ws/chat/(?P<chat_box_name>\w+)/$', consumers.Chatconsumer.as_asgi()),
]