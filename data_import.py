import os
from urllib.request import urlopen
import urllib.request

channel = "1477732"
start_date = "2021-09-08"
end_date = "2021-09-08"
start_time = "2012:00:00"
end_time = "2016:00:00"
file_name= channel+start_date +".csv"

URL = "https://api.thingspeak.com/channels/" + channel + "/feeds.csv?start=" +start_date +"%" +start_time + "&end=" +end_date +"%"+ end_time +"&timezone="+"Asia%2FKolkata"

print(URL)

urllib.request.urlretrieve(URL, file_name)
