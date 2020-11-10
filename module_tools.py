import datetime
import os
import webbrowser
import calendar
import random
import wikipedia

def open(text):
    text = text.lower();

    if 'youtube' in text:
        webbrowser.open("youtube.com")
    elif 'firefox' in text:
        os.system('start firefox.exe')
    elif 'cours' in text:
        webbrowser.open("itescia.blackboard.com")
        webbrowser.open("formations.cci-paris-idf.fr/IntNum/index.php/CAS")
    elif 'spotify' in text:
        os.system('start C:/Users/kille/AppData/Roaming/Spotify/spotify.exe')
    elif 'steam' in text:
        os.system('start C:/ProgramFiles(x86)/Steam/steam.exe')


    return "c'est fait"

def close(text):
    text = text.lower();
    if 'firefox' in text:
        os.system('taskkill /f /im firefox.exe')
    elif 'spotify' in text:
        os.system('taskkill /f /im spotify.exe')
    elif 'steam' in text:
        os.system('taskkill /f /im steam.exe')
    return "c'est fait"

def getDate():
    now = datetime.datetime.now()
    date = datetime.datetime.today()
    mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimache']
    return 'Nous sommes le ' + jours[date.weekday()] + " " + str(now.day) + ' ' + mois[now.month-1]
