"""
this is my cleanup branch
"""

import fb_main as fb
import spotify_main as spot
from datetime import date

fb_data = fb.get_artist(fb.get_usr_music())


def playlist_songs():
    playlist = []

    for artist in fb_data:
        try:
            spot_data = spot.get_top_tracks(spot.get_artist_id(artist))
            fb_data_date = fb.get_artist(fb.get_usr_music())[artist]  # the date user liked the artist

            for song in spot_data:
                playlist.append(song)

        except IndexError:
            pass

    return playlist[:99]  # first 100 songs - Spotify request can handle up to 100 uris


spot.add_track(spot.create_playlist(), playlist_songs())
