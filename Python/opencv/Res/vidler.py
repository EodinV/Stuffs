import yt_dlp


def name_it(url):
    sub = "video/"
    tit = url.find(sub)
    if tit != -1:
        return url[tit + len(sub):]
    else:     
        return url


# url input
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