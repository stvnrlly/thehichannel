# import re
import json
from datetime import datetime
# import logging
from channels import Group
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags.humanize import naturaltime
from his.models import Hi


@channel_session_user_from_http
def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group('hi-stream').add(message.reply_channel)


@channel_session_user
def ws_disconnect(message):
    Group('hi-stream').discard(message.reply_channel)


@channel_session_user
def ws_receive(message):
    # Check that the message is JSON
    try:
        data = json.loads(message['text'])
    except ValueError:
        return
    # Create hi and update channel
    # First, verify that the "sender" is the actual user
    if message.user.id == data['sender']:
        try:
            user = User.objects.get(id=data['sender'])
        except User.DoesNotExist:
            return
        hi = Hi.objects.create(
            message=data['message'],
            sender=user,
        )
        response = {
            'hi': 'hi',
            'sender': hi.sender.username,
            'timestamp': datetime.timestamp(hi.timestamp)
        }
        Group('hi-stream', channel_layer=message.channel_layer).send({
            'text': json.dumps(response)
        })
