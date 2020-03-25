from datetime import date
from datetime import datetime

x = date.fromisoformat('2000-03-20')
y = date.fromisoformat('1832-02-03')
z = date.fromisoformat('1852-02-03')
#zz = date.fromisoformat('1852-09-09').year

d1 = abs(x-y)
d2 = abs(y-z)

print(d1.days, d2.days)

#print(zz)

''''
date_delta = abs(date.fromisoformat(fb_data_date) - date.fromisoformat(spot_data[song])).days

                if date_delta < date_delta_min:
                    temp_song = song
                    playlist.append(song)
'''