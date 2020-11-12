import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

def commande(text):
    print("module spotify")
    if "suivante" in text or "suivant" in text or "suivante" in text:
        print("suivante")
        sp.next_track()
    elif "précédente" in text or "précédent" in text or "précédente" in text:
        print("précedente")
        sp.previous_track()
    elif "pause" in text or "ârrete" in text or "coupe" in text or "pose" in text:
        print("pause")
        sp.pause_playback()
        return "musique coupé"
    elif "reprend" in text or "lance" in text:
        print("lance")
        sp.start_playback()
        return "musique lancé"
    elif "son" in text or "volume" in text:
        volume(text)
    elif "recherche" in text:
        return recherche(text)
    elif ("qui" in text and "est") or ("nom" in text and("musique" in text or "chanson" in text)):
        return info()
    return ""


def info():
    print("info musique")
    musique = sp.current_user_playing_track()
    nom = musique["item"]["name"]
    artiste = musique["item"]["album"]["artists"][0]["name"]
    album = musique["item"]["album"]["name"]
    if musique["is_playing"] == "True":
        sp.pause_playback()
    return "Il s'agit de " + nom + " de " + artiste + " de l'album " + album
def volume(text):
    print("volume")
    if "maximum" in text:
        sp.volume(100)
    else:
        pct=[int(s) for s in text.split() if s.isdigit()]
        if len(pct)>0:
            sp.volume(pct[0])

def recherche(text):
    print("recherche")
    mots = text.split()
    mots[0]=''
    if mots[len(mots)-1] == "spotify" and mots[len(mots)-2] == "sur":
        mots[len(mots) - 1]=''
        mots[len(mots) - 2]=''
    req=""
    for m in mots:
        if m != "spotify" and m != "recherche":
            req+=m+' '
    print(req)
    res = sp.search(req,limit=5)
    sons = res["tracks"]["items"]
    if len(sons)==0:
        return "Aucun titres trouvé"

    if len(sons)==1:
        sp.start_playback(uris=[sons[0]["uri"]])
    else:
        sp.start_playback(uris=[sons[0]["uri"]])
    return ""
