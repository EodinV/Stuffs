import requests

response = requests.get("https://api.chucknorris.io/jokes/random")

prejoke = response.text.split("value")[1]
joke = prejoke.split(":")[1]
joke = joke[:-1]
print(joke)