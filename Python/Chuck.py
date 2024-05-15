import requests
import turtle

response = requests.get("https://api.chucknorris.io/jokes/random")

prejoke = response.text.split("value")[1]
joke = prejoke.split(":")[1]
joke = joke[:-1]
print(joke)

win = turtle.Screen()
win.setup(1200, 100)
win.bgcolor(0.6, 0.6, 0.6)
win.title("Is a Joke")

turtle.hideturtle()
turtle.write(joke, move=False, align="center", font=("Stencil", 13, "bold"))


turtle.done()