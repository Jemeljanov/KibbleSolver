import requests
import json

# Makes wrapping your head around it easier. As long as the code is kept flexible it will work with much bigger mazes too.
url = 'https://api.noopschallenge.com/mazebot/random?minSize=10&maxSize=10'
data = requests.get(url).json()
baremap = data['map']
starting_coordinates = data['startingPosition']