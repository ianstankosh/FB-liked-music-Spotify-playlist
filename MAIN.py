"""
- MAIN.py
- this is the main program for this project
- it uses the fb_main.py and spotify_main.py to gather liked FB songs to add to a Spotify playlist
"""

import fb_main as fb
import spotify_main as spot
from datetime import date

fb_data = fb.get_artist(fb.get_usr_music())  # {artist name: date of like}


def date_delta(fb_date, uri_date_dict):  # returns the Spotify track uri of most recent track compared to FB like date

    delta_dict = {}

    for entry in uri_date_dict:
        delta = abs(date.fromisoformat(fb_date) - date.fromisoformat(uri_date_dict[entry])).days
        delta_dict[delta] = entry

    min_date = min(delta_dict)
    return delta_dict[min_date]  # return Spotify track uri


def playlist_songs():

    playlist = []

    for artist in fb_data:
        try:  # in case artist liked on FB doesn't exist on Spotify
            spot_data = spot.get_top_tracks(spot.get_artist_id(artist))  # {track uri: date released, ...}
            fb_data_date = fb.get_artist(fb.get_usr_music())[artist]  # the date user liked the artist

            for song in spot_data:
                playlist.append(song)

            #playlist.append(date_delta(fb_data_date, spot_data))

        except IndexError:  # if the liked artist/music on FB doesn't exist on Spotify
            pass

    return playlist[:100]  # first 100 songs - Spotify request can handle up to 100 uris





spot.add_track(spot.create_playlist(), playlist_songs())
