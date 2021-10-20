import os
from urllib.request import urlopen
import urllib.request

channel = "1477732"
start_date = "2021-09-08"
end_date = "2021-09-08"
start_time = "2012:00:00"
end_time = "2016:00:00"
file_name= channel+start_date +".csv"

url = "https://api.thingspeak.com/channels/" + channel + "/feeds.csv?api_key=" +api_key +"&start=" +start_date +"%20" +start_time + "&end=" +end_date +"%20"+ end_time +"&timezone="+continent+"%2F"+city
s=requests.get(url).content
c=pd.read_csv(io.StringIO(s.decode('utf-8')))
a = c
x = c['created_at'].iloc[0].split(' ')[0]
y = c['created_at'].iloc[0].split(' ')[1]


while len(a) == 8000:
  if x != start_date and y != start_time :
    end_date = x 
    end_time = y
    url = "https://api.thingspeak.com/channels/" + channel + "/feeds.csv?api_key=" +api_key +"&start=" +start_date +"%20" +start_time + "&end=" +end_date +"%20"+ end_time +"&timezone="+continent+"%2F"+city
    s=requests.get(url).content
    a = pd.read_csv(io.StringIO(s.decode('utf-8')))
    c = a.merge(c, how = 'outer')
    x = c['created_at'].iloc[0].split(' ')[0]
    y = c['created_at'].iloc[0].split(' ')[1]
c.to_csv(filename)
