import requests

from config import TOKEN


class Slack:
    token   = TOKEN['Slack']
    url     = 'https://slack.com/api'
    headers = {'Authorization': f'Bearer {token}'}


    def __init__(self, channel, content):
        self.channel = channel
        self.content = content


    def get_channel_id(self):
        url = Slack.url + '/conversations.list'
        response = requests.get(
            url     = url,
            headers = Slack.headers
        ).json()

        channels = response['channels']

        for channel in channels:
            if channel['name'] == self.channel:
                return channel['id']
        return response


    def post_message(self):
        url = Slack.url + '/chat.postMessage'
        channel_id = self.get_channel_id()
        response   = requests.post(
            url     = url,
            headers = Slack.headers,
            data    = {'channel': channel_id, 'text': self.content}
        )

        return response

