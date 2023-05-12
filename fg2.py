#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from pytube import Search
import logging
import time
import datetime

logging.getLogger("pytube").setLevel(logging.ERROR)

def search_youtube_videos(query, max_results=10):
    search = Search(query)
    return search.results[:max_results]

def get_video_info(video):
    return {
        "title": video.title,
        "url": video.watch_url,
        "thumbnail_url": video.thumbnail_url,
    }

def display_video(video_info):
    st.image(video_info["thumbnail_url"], width=200)
    st.write(f"**[{video_info['title']}]({video_info['url']})**")
    st.write("---")

def compare_and_notify(new_videos, initial_videos, query):
    new_updates = []
    for video in new_videos:
        if video not in initial_videos:
            new_updates.append(video)
            st.experimental_rerun()
    return new_updates

search_queries = [
    "Howard Marks",
    "Ray Dalio",
    "Stanley Druckenmiller",
    "Alex Gurevich",
    "Curve Advisor",
]

st.title("Financial Gurus Video Dashboard")
st.sidebar.title("Search Settings")
max_results = st.sidebar.slider("Max Results", 1, 20, 5)

initial_videos = {}
for query in search_queries:
    initial_videos[query] = search_youtube_videos(query, max_results)

check_interval_seconds = 300
last_check_time = datetime.datetime.now()

st.header("Latest Videos")
for query in search_queries:
    st.subheader(query)
    videos = initial_videos[query]
    for video in videos:
        video_info = get_video_info(video)
        display_video(video_info)

st.header("New Updates")
while True:
    now = datetime.datetime.now()
    elapsed_time = now - last_check_time
    if elapsed_time.seconds > check_interval_seconds:
        for query in search_queries:
            new_videos = search_youtube_videos(query, max_results)
            new_updates = compare_and_notify(new_videos, initial_videos[query], query)
            if new_updates:
                st.subheader(query)
                for video in new_updates:
                    video_info = get_video_info(video)
                    display_video(video_info)
            initial_videos[query] = new_videos
        last_check_time = datetime.datetime.now()
    time.sleep(100)


# In[ ]:




