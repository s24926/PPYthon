import webbrowser
import Play_mp3
import requests as requests

filename = "robot_room.mp3"
Play_mp3.play(filename)

url = input("podaj adres strony")
webbrowser.open(url)

dates = ["20191111", "20191212", "20220101"]
for i in range (3):
    urls = "http://archive.org/wayback/available?url=" + url + "&timestamp=" + str(dates[i])
    response = requests.get(urls)
    d = response.json()
    page = d["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page)