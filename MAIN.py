"""
- MAIN.py
- this is the main program for this project
- it uses the fb_main.py and spotify_main.py to gather liked FB songs to add to a Spotify playlist
"""

import fb_main as fb
import spotify_main as spot
from datetime import date
import requests
import secrets
import sys


### checking if tokens are valid
fb_resp = requests.get(secrets.fb_url_main, params={'access_token': secrets.fb_access_token})
if fb_resp.status_code == 400:
    print("*****Expired Facebook Access Token*****")
    sys.exit()

resp = requests.get(secrets.spotify_url_main, headers={"Content-Type": "application/json", "Authorization": "Bearer {}".format(secrets.spotify_token)})
if resp.status_code == 401:
    print("*****Expired Spotify Access Token*****")
    sys.exit()


fb_data = fb.get_artist(fb.get_usr_music())  # {artist name: date of like}


def date_delta(fb_date, uri_date_dict):

    delta_dict = {}

    for entry in uri_date_dict:

        try:
            delta = abs(date.fromisoformat(fb_date) - date.fromisoformat(uri_date_dict[entry])).days
            delta_dict[delta] = entry

        except ValueError:  # in case FB or Spotify date is not in iso format, ie, 2012 or 12/03/95
            if len(uri_date_dict[entry]) is 4:  # if Spotify date is not iso format - '2012'
                uri_date_dict[entry] = uri_date_dict[entry] + '-01-01'
                delta = abs(date.fromisoformat(fb_date) - date.fromisoformat(uri_date_dict[entry])).days
                delta_dict[delta] = entry
            elif len(uri_date_dict[entry]) is 7:  # if Spotify date is not iso format - '2012-09'
                uri_date_dict[entry] = uri_date_dict[entry] + '-01'
                delta = abs(date.fromisoformat(fb_date) - date.fromisoformat(uri_date_dict[entry])).days
                delta_dict[delta] = entry
            else:
                delta = abs(date.fromisoformat(fb_date) - date.today()).days  # if something else is wrong
                delta_dict[delta] = entry

    min_date = min(delta_dict)
    return delta_dict[min_date]  # return spotify track uri


def playlist_songs():

    playlist = []

    for artist in fb_data:
        try:  # in case artist liked on FB doesn't exist on Spotify
            spot_data = spot.get_top_tracks(spot.get_artist_id(artist))  # {track uri: date released, ...}
            fb_data_date = fb.get_artist(fb.get_usr_music())[artist]  # the date user liked the artist

            playlist.append(date_delta(fb_data_date, spot_data))

        except IndexError:  # if the liked artist/music on FB doesn't exist on Spotify
            pass

    return playlist[:100]  # first 100 songs - Spotify request can handle up to 100 uris


spot.add_track(spot.create_playlist(), playlist_songs())
