import requests
import os
from pyquery import PyQuery as pq


def getTitle(app):
    url = "https://store.steampowered.com/app/" + str(app)

    headers = {
        "cookie": "Steam_Language=schinese"
    }
    response = requests.get(url, headers=headers)

    doc = pq(response.text)

    title = doc("#appHubAppName").text()
    return title


def rename():
    dirList = os.listdir()
    print(dirList)
    for i in dirList:
        if i == "rename.py" or i == "rename.exe":
            break
        try:
            name = getTitle(i)
            print(i + "---->" + name)
            os.rename(i, name)
        except FileNotFoundError:
            pass


rename()
