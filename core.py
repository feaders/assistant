import speech_recognition as sr
import warnings
import pyttsx3

import random
import time

import module_users as mu
import module_spotify as ms
import module_attestation as ma
import module_tools as mt
import config

print('Initialisation')
mu.loadUsers()

active = True
engine = pyttsx3.init()
voice = engine.getProperty('voices')[0]  # the french voice
engine.setProperty('voice', voice.id)
warnings.filterwarnings('ignore')


def audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    data = ''
    try:
        data = r.recognize_google(audio, None, "fr-FR")
        print('Vous avez dit:' + data)
    except sr.UnknownValueError:
        print('Erreur')
    except sr.RequestError as e:
        print('Erreur requete')
    return data.lower()


def reponse(text):
    engine.say(text)  # perfect
    engine.runAndWait()


def motActivation(text):
    MOTS = ['hey billy', 'dit billy', 'ok billy', 'activation billy', 'billy']
    text = text.lower()
    for phrase in MOTS:
        if phrase in text:
            return True
    return False


def salutations(text):
    formules = ['bonjour', 'wesh', 'yo']

    formulesReponse = ['bonjour', 'wesh', 'yo']

    for word in text.split():
        if word.lower() in formules:
            return random.choice(formulesReponse) + '. '
    return ''


def extinction():
    formulesReponse = ['A la prochaine', 'a plus', 'Billy out']
    reponse(random.choice(formulesReponse))
    print("je m'eteint")


print("billy prêt")
reponse("je suis prêt")

while active == True:
    text = audio()
    rep = ''

    if motActivation(text) == True:
        rep += salutations(text)
        if 'date' in text or 'jour' in text:
            rep += mt.getDate()
        elif 'ouvre' in text:
            rep += mt.open(text)
        elif 'ferme' in text:
            rep += mt.close(text)
        elif 'attestation' in text:
            rep += ma.genrerAttestation(text)
        elif 'extinction' in text:
            extinction()
            break
        elif 'spotify' in text or config.getConfig().spotify == False:
            rep += ms.commande(text)

    if rep != '':
        reponse(rep)
