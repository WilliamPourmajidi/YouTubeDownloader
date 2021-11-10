from pytube import YouTube

#where to save
SAVE_PATH = "C:/MyFolder" 

#link of the video to be downloaded


#Use a list  ["https://youtu.be/G1233123123123",""https://youtu.be/GhZi12312312354"]

links = []
     
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
     
print('All downloads are Completed!')

