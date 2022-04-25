from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
from .models import *
from channels.db import database_sync_to_async
import datetime

class MyJsonWebSocketConsumer(JsonWebsocketConsumer) :
    def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()
        # self.close()    #to reject the connection request

    def receive_json(self, content, **kwargs) :
        # print('content...', content)
        group = Group.objects.get(unique_id=self.group_name)
        if self.scope['user'].is_authenticated :
            chat = Chat(
                content = content['msg'],
                group = group,
                sender = self.scope['user']
            )
            chat.save()
            content['user'] = self.scope['user'].username
            content['dt'] = str(datetime.datetime.now())[10:16:]
            # print(datetime.time())
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    'type' : 'chat.message',
                    'message' : content
                }
            )
        else:
            self.send_json({
                'message' : 'Login Required'
            })

    def chat_message(self, event) :
        self.send_json({
            'message' : event['message']
        })

    def disconnect(self, close_code) :
        # print(close_code)
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)




class MyAsyncJsonWebSocketConsumer(AsyncJsonWebsocketConsumer) :
    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def receive_json(self, content, **kwargs) :
        # print('content...', content)

        group = await database_sync_to_async(Group.objects.get)(name=self.group_name)
        chat = Chat(
            content = content['msg'],
            group = group
        )
        await database_sync_to_async(chat.save)()

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type' : 'chat.message',
                'message' : content['msg']
            }
        )

    async def chat_message(self, event) :
        await self.send_json({
            'message' : event['message']
        })

    async def disconnect(self, close_code) :
        # print(close_code)
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
