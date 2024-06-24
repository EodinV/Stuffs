from duckduckgo_search import DDGS
import discord as dis
import os


#Video search correspondence
def VidDuck(quey):
    links = []
    qu = quey.split(":")
    query = qu[1]
    results = DDGS().videos(
    keywords=query,
    region="wt-wt",
    safesearch="moderate",
    resolution="high",
    max_results=3)
    for result in results:
        content = result.get("content")
        if content:
            links.append(content)
    return(links)

#Image search API correspondence
def ImgDuck(quey):
    links = []
    qu = quey.split(":")
    query = qu[1]
    results = DDGS().images(
    keywords=query,
    region="wt-wt",
    safesearch="moderate",
    size=None,
    max_results=3)
    for result in results:
        content = result.get("image")
        if content:
            links.append(content)
    return(links)

#Search API correspondence
def SearchDuck(quey):
    links = []
    qu = quey.split(":")
    query = qu[1]
    results = DDGS().text(
    query, 
    region='wt-wt', 
    safesearch='moderate', 
    timelimit='y', 
    max_results=10)
    for result in results:
        content = result.get("href")
        if content:
            links.append(content)
    return(links)

#News API correspondence
def NewsDuck(quey):
    links = []
    qu = quey.split(":")
    query = qu[1]
    results = DDGS().news(
    keywords = query,
    safesearch = "moderate",
    max_results = 10)
    for result in results:
        content = result.get("url")
        if content:
            links.append(content)
    return(links)

#ChatGPT LLM correspondence
def AIDuckGPT(quey):
    qu = quey.split(":")
    query = qu[1]
    answer = DDGS().chat(
        keywords = query,
        model = "gpt-3.5"
    )
    return(answer)

#Claude LLM correspondence
def AIDuckHaiku(quey):
    qu = quey.split(":")
    query = qu[1]
    answer = DDGS().chat(
        keywords = query,
        model = "claude-3-haiku"
    )
    return(answer)

#Llama LLM correspondence
def AIDuckllama(quey):
    qu = quey.split(":")
    query = qu[1]
    answer = DDGS().chat(
        keywords = query,
        model = "llama-3-70b"
    )
    return(answer)

#Mixtral LLM correspondence
def AIDuckMixtral(quey):
    qu = quey.split(":")
    query = qu[1]
    answer = DDGS().chat(
        keywords = query,
        model = "mixtral-8x7b"
    )
    return(answer)

#Response to --help in chat
def help():
    pleh = "Begin message with:\n\"Search:\" for a Websearch\n\"News:\" for News\n\"Image:\" for an Imagesearch\n\"Video:\" for a Videosearch\n\"GPT:\" for an LLM query (gpt-3.5)\n\"Haiku:\" for an LLM query (claude-3-haiku)\n\"Llama:\" for an LLM query (llama-3-70b)\n\"Mixtral:\" for an LLM query (mixtral-8x7b)"
    return(pleh)

print(os.getenv('DISCORD_TOKEN'))

client = dis.Client(intents = dis.Intents.all())

#Login
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == os.getenv('DISCORD_GUILD'):
            break
        
    print('We have logged in as {0.user}'.format(client))

#Listen and respond
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'Video:' in message.content: 
        joke = VidDuck(message.content)
        await message.channel.send(joke)

    if 'Image:' in message.content: 
        joke = ImgDuck(message.content)
        await message.channel.send(joke)

    if 'Search:' in message.content: 
        joke = SearchDuck(message.content)
        await message.channel.send(joke)

    if 'News:' in message.content: 
        joke = NewsDuck(message.content)
        await message.channel.send(joke)

    if 'GPT:' in message.content: 
        joke = AIDuckGPT(message.content)
        await message.channel.send(joke)

    if 'Haiku:' in message.content: 
        joke = AIDuckHaiku(message.content)
        await message.channel.send(joke)

    if 'Llama:' in message.content: 
        joke = AIDuckllama(message.content)
        await message.channel.send(joke)

    if 'Mixtral:' in message.content: 
        joke = AIDuckMixtral(message.content)
        await message.channel.send(joke)

    if '--help' in message.content:
        joke = help()
        await message.channel.send(joke)

#Token    
client.run('Discord Token')