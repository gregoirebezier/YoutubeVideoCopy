#!/usr/bin/python3
import pyperclip
from time import sleep
from api.worker import celery

def GetLink():
    return pyperclip.paste()

def GetYoutubeCopy():
    PreviousLink = ""
    while (1):
        try:
            link = GetLink()
            if (link[:32] == "https://www.youtube.com/watch?v=" and PreviousLink != link):
                celery.send_task('tasks.GetYoutube', args=[link], kwargs={})
                PreviousLink = link
        except:
            sleep(1)
GetYoutubeCopy()