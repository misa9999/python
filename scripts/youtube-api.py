#!/user/bin/env python3
import json

from apiclient.discovery import build


api_key = ""


youtube = build('youtube', 'v3', developerKey=api_key)


def write_json(data):
    with open('output.json', 'w') as f:
        json.dump(data, f)


def get_channel_videos(channel_id):
    res = youtube.channels().list(id=channel_id,
                                  part="contentDetails").execute()

    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    next_page_token = None

    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id,
                                           part="snippet",
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')

        if next_page_token is None:
            break

    return videos


videos = get_channel_videos('UCK5tosXMdCitAX8ef7j5c9w')

url = 'https://www.youtube.com/watch?v='

links = []

for video in videos:
    link = url+video['snippet']['resourceId']['videoId']
    print(link)
    links.append(link)


# req = youtube.search().list(q='waifu', part='snippet', type='video', maxResults=50)
# req = youtube.search().list(q='ANTRAZ MENTALZ', part='snippet',
#                             type='channel', maxResults=50)
# res = req.execute()

# for item in res['items']:
#     print(item['snippet'])

# 'channelId': 'UCK5tosXMdCitAX8ef7j5c9w',
