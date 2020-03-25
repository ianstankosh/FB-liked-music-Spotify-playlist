"""
- this program has functions to create a new playlist on Spotify, get artists' id #s,
retrieve an artist's top 10 songs from Spotify, add song to the playlist
"""

import requests
import secrets
import json


def create_playlist():  # creates playlist and returns playlist id

    request_body = json.dumps({
        "name": "Liked FB Music",
        "description": "This playlist contains songs from the user's liked musical artists on Facebook.",
        "public": True
    })

    query = secrets.spotify_url_main + 'users/' + secrets.spotify_usr_id + '/playlists'
    resp = requests.post(
        query,
        data=request_body,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(secrets.spotify_token)
        }
    )

    resp_json = resp.json()
    return resp_json["id"]  # id of Sptify playlist


def get_artist_id(search_query):  # this is going to take the output from fb_main

    query = secrets.spotify_url_main + 'search'
    resp = requests.get(
        query,
        params={"q": search_query,
                "type": "artist",
                "limit": "1",
                "offset": "0"},
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(secrets.spotify_token)
        }
    )

    resp_json = resp.json()
    artist_id = resp_json['artists']['items'][0]['id']
    return artist_id  # artist id


def get_top_tracks(artist_id):  # returns a dict of top song: date released

    query = secrets.spotify_url_main + 'artists/' + artist_id + '/top-tracks'
    resp = requests.get(
        query,
        params={"country": "US"},
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(secrets.spotify_token)
        }
    )

    resp_json = resp.json()
    top_tracks = resp_json

    song_dict = {}
    for song_info in top_tracks['tracks']:
        song_dict[song_info['uri']] = song_info['album'][
            'release_date']  # dict of song title uri: date released, starting with top song
    return song_dict


def add_track(playlist_id, uris):  # uri can be a comma separated list

    request_body = json.dumps({"uris": uris})

    query = secrets.spotify_url_main + 'playlists/' + playlist_id + '/' + 'tracks'
    resp = requests.post(
        query,
        data=request_body,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(secrets.spotify_token)
        }
    )
    resp_json = resp.json()

    return resp_json


#print(create_playlist())

# print(get_top_tracks(get_artist_id('Vampire Weekend')))


uris = ['spotify:track:39exKIvycQDgs4T6uXdyu0', 'spotify:track:1595LW73XBxkRk2ciQOHfr', 'spotify:track:4dRqYKhLVujxiBXcq50YzG', 'spotify:track:53KFMdxzi8IJDewiql1Qo3', 'spotify:track:78J9MBkAoqfvyeEpQKJDzD', 'spotify:track:7psPPGwhFzP3pyOcb3ivcT', 'spotify:track:2FjoCQaBoiEKs3FCvD0HkR', 'spotify:track:3t87C08isN6yw2DnWOorLm', 'spotify:track:7lQgoAWAFAo0XW7dW2TL1y', 'spotify:track:2Ml0l8YWJLQhPrRDLpQaDM']
add_track(create_playlist(), uris)
