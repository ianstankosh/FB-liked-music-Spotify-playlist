from datetime import date
from datetime import datetime

x = date.fromisoformat('2000-03-20')
y = date.fromisoformat('1832-02-03')
z = date.fromisoformat('1852-02-03')
#zz = date.fromisoformat('1852-09-09').year

d1 = abs(x-y)
d2 = abs(y-z)

#print(d1.days, d2.days)

#print(zz)


def date_delta(fb_date, uri_date_dict):

    delta_dict = {}

    for entry in uri_date_dict:

        try:
            delta = abs(date.fromisoformat(fb_date) - date.fromisoformat(uri_date_dict[entry])).days
            delta_dict[delta] = entry
        except ValueError:  # in case FB date is not in iso format, ie, 2012 or 12/03/95
            print('value error')
            delta = 0
            delta_dict[delta] = entry

    min_date = min(delta_dict)
    return delta_dict[min_date]  # return spotify track uri


print(date_delta('jfj', {'spot:track:hgjasnsdjlg': '2020', 'spot:track:XXnsdjlg': '2020-03-24', 'spot:track:BBsdjlg': '2020-03-13'}))

#print(date.today())
