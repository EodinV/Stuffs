import yt_dlp
import os
import glob

# Purge video files (could be extended):
def purge():
    extensions = ['*.mp4', '*.avi', '*.mpg']
    for ext in extensions:
        for file in glob.glob(ext):
            try:
                os.remove(file)
                print(f"Deleted: {file}")
            except Exception as e:
                print(f"Error deleting {file}: {e}")

    print("All known video files have been deleted.")

def name_it(url):
    sub = "video/"
    tit = url.find(sub)
    if tit != -1:
        return url[tit + len(sub):]
    else:     
        return url


# url input
def downl():
    video_url = input("Http: ")
    nameis = input("Name it?: (y/n) ...recommended ")
    if nameis == "y" or nameis == "Y":
        name = input("Name it!  : ")        
    else: name = name_it(f"{video_url}")
    # Set options for downloading
    ydl_opts = {
        'format': 'best',  # Download the best quality
        'outtmpl': f'{name[-25:]}.%(ext)s',  # Output filename template
    }

# Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

act = input("Download or purge? d/p:  ")
if act == "d" or act == "D":
    downl()
elif act == "p" or act == "p":
    sure = input("Are you sure) y/n:  ")
    if sure == "y" or sure == "Y":
        purge()
    else: 
        print("Closing...")
        quit()