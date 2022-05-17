import csv
import html
import os
import time
import requests
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import googleapiclient.discovery

com_ls = []
vid_ls = []
vid = ''

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    getVideos()

def getVideos():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.search().list(
        part="snippet",
        maxResults=10,
        order="viewCount",
        q="satoshi nakamoto",
        regionCode="FR",
        relevanceLanguage="EN"
    )
    response = request.execute()
    #print(response)

    for vid in response.get('items', {}): 
        video = vid['id']['videoId']
        vid_ls.append(video)
        #print(vid_ls)

    getComments()


def getComments():
    for vid in vid_ls:
        #create_app(vid)
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = "AIzaSyDa7vpFgeOxqeNgHUjCqxC5kkrSUphuN5k"

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = DEVELOPER_KEY)

        request = youtube.commentThreads().list(
            part="snippet",
            maxResults=50,
            searchTerms="-video, -explanation, -black people, -explained, -explain, -episode, -comments",
            videoId = vid
        )
        response = request.execute()

        for com in response.get('items', {}): 
            com = com['snippet']['topLevelComment']['snippet']['textDisplay']
            if len(com) < 206:
                com = com.encode("ascii", "ignore")
                com = com.decode()
                com = html.unescape(com)
                comment = [com] 
                com_ls.append(comment)

        #string = com_ls[1]
        #print(string)
        for com in com_ls:
            time.sleep(0.5) 
            print(str('videoID ') + vid + str(': new comment added'))
        
        toCSV(com_ls)
        time.sleep(2)
        #com_ls.clear()

def toCSV(data):
    # open the file in the write mode
    with open('data.csv', 'a', encoding='ascii') as f:
        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        writer.writerows(data)  

if __name__ == "__main__":
    main()

