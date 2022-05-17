# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import time
import serial

from flask import Flask, render_template
#app = Flask(__name__)

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# declare arduino port
arduino = serial.Serial(port='/dev/cu.usbmodem14301', baudrate=38400)

# declare array to store comments and 
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
        q="blockchain",
        regionCode="FR",
        relevanceLanguage="EN"
    )
    response = request.execute()
    #print(response)

    for vid in response.get('items', {}): 
        video = vid['id']['videoId']
        vid_ls.append(video)
        print(vid_ls)

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
            searchTerms="blockchain, -her, -she, -video, -explanation, -black people, -explained",
            videoId = vid
        )
        response = request.execute()

        for com in response.get('items', {}): 
            comment = com['snippet']['topLevelComment']['snippet']['textDisplay']
            if len(comment) < 206:
                com_ls.append(comment)

        #string = com_ls[1]
        #print(string)
        for com in com_ls:
            time.sleep(2) 
            print(str('videoID ') + vid + str(': ') + com)
            arduino.write(com.encode('utf-8'))
        
        time.sleep(10)
        com_ls.clear()

    

if __name__ == "__main__":
    main()



