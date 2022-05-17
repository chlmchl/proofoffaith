# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import time
import requests
import json
import serial

# import google API libs
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import googleapiclient.discovery

# declare arduino port
arduino = serial.Serial(port='/dev/cu.usbmodem214301', baudrate=38400)

# declare array to store comments
com_ls = []

# get comments from youtube video
def main():
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
        maxResults=20,
        searchTerms="blockchain, -her, -she, -video",
        videoId="sDNN0uH2Z3o"
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
        print(com)
        arduino.write(com.encode('utf-8'))

    #print(response.keys())

if __name__ == "__main__":
    main()
    