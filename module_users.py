import json
import os

USERS=[]
dir="./CONFIG/USERS/"
class user:
    def __init__(self, appelation, nom, prenom, datenNaissance, adresse, ville, cp, mail):
        self.appelation = appelation
        self.nom = nom
        self.prenom = prenom
        self.datenNaissance = datenNaissance
        self.adresse = adresse
        self.ville = ville
        self.cp = cp
        self.mail = mail



def load(filename):
    user_dict = json.loads(filename)
    user_object = user(**user_dict)
    USERS.append(user_object)

def loadUsers():
    for f in filter(lambda x: x.endwith('.json'),os.listdir(dir)):
        load(f)
    print(USERS)