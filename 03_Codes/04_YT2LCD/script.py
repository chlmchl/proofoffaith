# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import requests
import json

import googleapiclient.discovery

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
        print(com['snippet']['topLevelComment']['snippet']['textDisplay'])

    #print(response.keys())

if __name__ == "__main__":
    main()

    