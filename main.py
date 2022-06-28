import requests
import json

#Get Input
channel_name = input("Please input name of YouTube Channel to search: ")
r = requests.get(f'https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&forUsername={channel_name}&key=AIzaSyCjRbmEAeEe35cuqAsoJ7Zn80ukUx0FQjQ')
data = r.json()

#Print
if data['pageInfo']['totalResults'] != 0:
  item = data['items'][0]['statistics']
  print(f"{channel_name} has {item['subscriberCount']} subscribers, {item['videoCount']} total videos and a grand sum of {item['viewCount']} across their whole channel!")
else:
  print("Either that YouTube Channel does not exists or they are not big enough to be searched by name. Please try again.")