from django.urls import path
from .consumers import *

# websocket_urlpatterns = [
#     path("ws/chatroom/<chatroom_name>", ChatroomConsumer.as_asgi()),
#     path("ws/private_chat/<chatroom_name>", PrivateChatConsumer.as_asgi())
# ]
websocket_urlpatterns = [
    path("ws/chat/room/<str:chatroom_name>/", ChatroomConsumer.as_asgi()),
]
