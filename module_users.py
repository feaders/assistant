import json
import os
import CONFIG

USERS=[]
dir="./CONFIG/USERS/"
class user:
    def __init__(self, username, nom, prenom, datenNaissance,lieuNaissance, adresse, ville, cp, mail):
        self.username = username
        self.nom = nom
        self.prenom = prenom
        self.datenNaissance = datenNaissance
        self.lieuNaissance = lieuNaissance
        self.adresse = adresse
        self.ville = ville
        self.cp = cp
        self.mail = mail



def load(filename):
    user_dict = json.loads((open(dir + filename, "r")).read())
    user_object = user(**user_dict)
    USERS.append(user_object)

def loadUsers():
    for f in filter(lambda x: x.endswith('.json'),os.listdir(dir)):
        load(f)
    print("Users:")
    print("/////////////////")
    for x in USERS:
        print(x.username)
    print("/////////////////")
def getUser(text):
    mots = text.split()
    for m in mots:
        for x in USERS:
            if x.username == m:
                return x
    return getDefault()

def getDefault():
    for x in USERS:
        if x.username == CONFIG.getConfig().user:
            return x