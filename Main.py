from pytube import YouTube
from pytube import Playlist
import re

#where to save
SAVE_PATH = "C:/MyVideos" 

# please note that the playlist must be public
playlist = Playlist('https://www.youtube.com/playlist?list=PLzwWSJNcZTMSW-v1x6MhHFKkwrGaEgQ-L')


# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))

to_be_downloaded_list = []

for url in playlist.video_urls:
    print(url)
    to_be_downloaded_list.append(url)



# If you have a few videos use the following, otherwise, put the playlist in playlist variable (above)    
# links = ['https://www.youtube.com/watch?v=xCqbufBv3Lk&list=PLjVtv4TPnrcJ7JAyNbTY3qmNxnIwBqr85&index=144','https://www.youtube.com/watch?v=FemlaDqXxos&list=PLjVtv4TPnrcJ7JAyNbTY3qmNxnIwBqr85&index=141']

links = to_be_downloaded_list
     
for link in links:
    try:         
        # object creation using YouTube
        # which was imported in the beginning
        video = YouTube(link)
        print(f"## Connection to {link} Succesfull!!")
        print(f"## Now Downloading: {video.title}")
        
        print(f"## This is the ranking of this video: {video.rating}")
        print(f"## This is the duration of this video: {video.length/60} minutes! ")
        
        
       
        video.streams.get_highest_resolution().download(SAVE_PATH) 
        print(f"## Completed Download for: {video.title}") 
    except:
        #to handle exception
        print("Connection Error")
     
print('Task Completed!')

# # physically downloading the audio track
# for video in playlist.videos:
#     audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
#     audioStream.download(output_path=DOWNLOAD_DIR)
