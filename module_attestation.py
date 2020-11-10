from reportlab.pdfgen import  canvas
from datetime import datetime
import pyqrcode
import module_mail as mm

dt_stamp = datetime.now()
image = "canvas.png"
imageQr = "qr.png"

def genrerAttestation(text):
    raisons = {
        'travail': 578,
        'courses': 533,
        'course': 533,
        'sante': 477,
        'famille': 435,
        'handicap': 396,
        'sport_animaux': 358,
        'sport': 358,
        'convocation': 295,
        'missions': 255,
        'enfants': 211,
    }

    croix = []
    for r in raisons:
        if r in text:
            croix.append(raisons[r])

    nom = "William"
    prenom = "Bouhaik"
    datenaiss = "14/01/2000"
    lieuxnaiss = "Pontoise"
    adresse = "Résidence la voie du sud"
    ville = "Longjumeau"
    cp = "91160"
    date = str(dt_stamp.strftime('%d/%m/%Y'))
    heure = str(dt_stamp.strftime("%H:%M"))

    textQR = "Cree le: " + date +" a "+heure+"; Nom:"+nom+"; Prenom:"+prenom+"; naissance"+datenaiss+" a "+lieuxnaiss+ "; Adresse: " + adresse + " " + cp+" "+ville+";"
    qr = pyqrcode.create(textQR)
    qr.png("qr.png",scale=10)

    nomFichier = "attestation-"+str(dt_stamp.strftime('%d-%m-%Y'))+".pdf"
    pdf = canvas.Canvas(nomFichier)
    pdf.setTitle('COVID-19 - Déclaration de déplacement')
    pdf.setSubject('Attestation de déplacement dérogatoire')
    pdf.setAuthor("Ministère de l'intérieur")
    pdf.setKeywords([
    'covid19',
    'covid-19',
    'attestation',
    'déclaration',
    'déplacement',
    'officielle',
    'gouvernement',
  ])
    pdf.drawImage(image, -25, 5, 215*3, 279*3)

    pdf.drawString(119, 696, prenom + " " + nom)
    pdf.drawString(119, 674, datenaiss)
    pdf.drawString(297, 674, lieuxnaiss)
    pdf.drawString(133, 652, adresse+", " + cp + " " + ville.upper())

    for i in croix:
        pdf.drawString(62, i, 'x')

    pdf.drawString(105, 177, ville)
    pdf.drawString(91, 155, date)
    pdf.drawString(255, 155, heure)
    pdf.drawImage(imageQr, 435, 110, 92, 92)

    pdf.save()
    mm.sendAttestation(nomFichier)
    return "attestation générer"