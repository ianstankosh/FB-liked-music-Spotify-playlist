"""
This program returns a Facebook user's liked music artists in a dictionary(artist: date of like)
"""

# "https://graph.facebook.com/{your-user-id}?fields=id,name&access_token={your-user-access-token}"
# fields must be one or more strings separated by commas with no spaces in between

# must re-generate token every few hours

import requests
import json
import secrets
from secrets import fb_access_token


def get_usr_music():
    base_url = secrets.fb_url_main
    params_dict = {'fields': 'music', 'access_token': fb_access_token}

    resp = requests.get(base_url, params=params_dict)

    return resp.json()['music']


def get_artist(data, artist_dict=None):

    if artist_dict is None:
        artist_dict = {}

    for artist in data['data']:
        name = artist['name']
        date = artist['created_time'][:10]  # YYYY-MM-DD
        artist_dict[name] = date

    try:
        next_resp = data['paging']['next']
        next_req = requests.get(next_resp).json()
        get_artist(next_req, artist_dict)
        return artist_dict  # returns dictionary of artist name: date of like
    except:
        pass


print(get_artist(get_usr_music()))
