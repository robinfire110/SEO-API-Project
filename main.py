import requests
import json
import sqlalchemy as db
import pandas as pd

#Get Channel Data
#Tests: Put in non-id/names
def get_channel_data(input):
  #Check Name
  r = requests.get(f'https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&forUsername={input}&key=AIzaSyCjRbmEAeEe35cuqAsoJ7Zn80ukUx0FQjQ')
  data = r.json()
  if data['pageInfo']['totalResults'] != 0: 
    return data

  #Check ID
  r = requests.get(f'https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id={input}&key=AIzaSyCjRbmEAeEe35cuqAsoJ7Zn80ukUx0FQjQ')
  data = r.json()
  if data['pageInfo']['totalResults'] != 0: 
    return data

  #Return
  return data

#Print Data
def print_channel_data(data):
  if data['pageInfo']['totalResults'] != 0:
    item = data['items'][0]['statistics']
    channel_name = data['items'][0]['snippet']['title']
    print(f"{channel_name} has {item['subscriberCount']} subscribers, {item['videoCount']} total videos and a grand sum of {item['viewCount']} across their whole channel!")
    return True
  else:
    print("Either that YouTube Channel does not exists or they are not big enough to be searched by name. Please try again.")
    return False

#Put Data into Dataframe
def data_to_dataframe(data):
  if data['pageInfo']['totalResults'] != 0:
    dataframe = pd.DataFrame(data['items'][0])
    dataframe.drop(labels=['thumbnails', 'localized', 'relatedPlaylists'], axis = 0, inplace = True)
    return dataframe
  else:
    return False

#Put Dataframe into SQL
def dataframe_to_sql(engine, df):
  try:
    df.to_sql('channel_stats', con=engine, if_exists='replace')
    query_result = engine.execute("SELECT * FROM channel_stats;").fetchall()
    print(pd.DataFrame(query_result))
    return True
  except:
    print("An error occured.")
    return False

#Run Program 
channel_name = input("Please input name of YouTube Channel to search: ")
data = get_channel_data(channel_name)
if print_channel_data(data):
  df = data_to_dataframe(data)
  engine = db.create_engine('sqlite:///data_base_name.db')
  dataframe_to_sql(engine, df)