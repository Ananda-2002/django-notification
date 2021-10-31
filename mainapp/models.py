from django.db import models
from django.db.models.signals import post_save
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync, sync_to_async
from django.dispatch import receiver
import json

# Create your models here.
PERCENTAGE_CHOICES = (
    ('20', '20'),
    ('40', '40'),
    ('60', '60'),
    ('80', '80'),
    ('100', '100')
)


class percentage(models.Model):
    percentage = models.CharField(
        max_length=3, choices=PERCENTAGE_CHOICES, default='20')

    def __str__(self):
        return self.percentage

    @staticmethod
    def give_percentage_details(id):
        instance = percentage.objects.get(id=id)
        data = {}
        data['id'] = id
        data['percentage'] = instance.percentage
        return data


@receiver(post_save, sender=percentage)
def _percentage_save_receiver(sender, instance, created, **kwargs):
    if not created:
        channel_layer = get_channel_layer()
        data = {}
        data['id'] = instance.id
        data['percentage'] = instance.percentage
        print('hii')
        print(data)
        async_to_sync(channel_layer.group_send)(
            'order_%s' % instance.id,
            {
                'type': 'percentage_status',
                'value': json.dumps(data)
            }
        )
