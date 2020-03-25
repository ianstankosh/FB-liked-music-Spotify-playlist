#this is my cleanup branch

import fb_main as fb
import spotify_main as spot
from datetime import date

fb_data = fb.get_artist(fb.get_usr_music())
#print(fb_data)


def playlist_songs():

    playlist = []

    for artist in fb_data:
        try:
            spot_data = spot.get_top_tracks(spot.get_artist_id(artist))
            fb_data_date = fb.get_artist(fb.get_usr_music())[artist]  # the date user liked the artist
            #print(fb_data_date)
            #print(spot_data)

            for song in spot_data:
                #print(spot_data[song])  # date of each top 10 song starting with most popular
                #print(song)
                playlist.append(song)

        except IndexError:
            pass

    return playlist[:99]  #  first 100 songs - spotify request can handle up to 100 uris


#print(playlist_songs())
spot.add_track(spot.create_playlist(), playlist_songs())
