import random
import webbrowser
import requests

CHARLES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
charles = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
intgrid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', '-']

video = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
status = 0
iteration = 0

while status == 0:
    for i in range(11):
        videocode = ''
        randwhat = random.randrange(start=0, stop=2)
        randchar = random.randrange(start=0, stop=25)
        randCHAR = random.randrange(start=0, stop=25)
        randint = random.randrange(start=0, stop=11)
    
        if randwhat == 0:
            video[i] = charles[randchar]
        
        elif randwhat == 1:
            video[i] = CHARLES[randchar]
        
        elif randwhat == 2:
            video[i] = intgrid[randint]
        
    videocode = videocode.join(video)
    thing = requests.get(f'https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={videocode}&format=json')
    iteration = iteration + 1
    
    print(f'Iteration: {iteration}, Status code: {thing.status_code}')

    if thing.status_code == 200:

        webbrowser.open(f'https://www.youtube.com/watch?v={videocode}')
        status = 1


