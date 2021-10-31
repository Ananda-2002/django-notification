from channels.generic.websocket import WebsocketConsumer
import json
from .models import percentage
from channels.generic.websocket import WebsocketConsumer
import json
from .models import percentage
from asgiref.sync import async_to_sync, sync_to_async


class Progress(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['id']
        self.room_group_name = 'order_%s' % self.room_name
        _id = self.room_name
        print("connect")
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        data = percentage.give_percentage_details(_id)
        print(data)
        self.send(text_data=json.dumps({'payload': data}))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'percentage_status',
                'payload': text_data
            }
        )

    def percentage_status(self, event):
        print('hello')
        print(event)
        data = json.loads(event['value'])
        self.send(text_data=json.dumps({
            'payload': data
        }))
