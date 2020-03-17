from urllib.request import urlopen
import json
import datetime

print("Welcome to cuz-weather")
date = datetime.datetime.today()
date = date.strftime("%Y/%-m/%-d")

usersearch = input("Where would you like to check the weather?\n>")

link = 'https://www.metaweather.com/api/location/search/?query=' + usersearch
response = urlopen(link)
data = json.loads(response.read())
woeid = data[0]['woeid']

link = "https://www.metaweather.com/api/location/" + str(woeid) + date
response = urlopen(link)
data = json.loads(response.read())

print(data[0]['woeid'])
