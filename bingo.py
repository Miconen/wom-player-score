import requests
from Player import Player
import time

playersFile = open('players.txt', 'r')
lines = playersFile.readlines()
playersFile.close()
players: list[Player] = []

for line in lines:
    time.sleep(2)
    try:
        response = requests.get("https://api.wiseoldman.net/v2/players/search?username=" + line).json()[0]
        player = Player(response)
        print(f"Fetching {line.strip()}...")
        players.append(player)
    except:
        print("Skipped " + line.strip())
        continue

players.sort(reverse=True)

for i, player in enumerate(players):
    print(f"#{i + 1} {player}")
