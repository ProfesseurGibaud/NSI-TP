import random
import os
import numpy as np
root = os.getcwd() #Naviguer avant de lancer le programme sinon ça va envahir votre dossier utilisateur

File = []
Compteur = 0
Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def MkDos(p,path): #path chemin dossier, p proba de créer un dossier
    global File,Compteur
    os.chdir(path)
    u = random.random()
    v = random.random()
    while u<p:
        print("Création")
        os.mkdir(str(Compteur))
        os.chdir(str(Compteur))
        # Ajouter ouvrir document avec proba v et écrire Alphabet[compteur%26]
        temp_path = os.getcwd()
        File.append(temp_path)
        os.chdir("..")
        u = random.random()
        Compteur +=1
    os.chdir(root)


def Boucle(p,t): #p proba initiale, t taux de décroissance
    global File,Compteur
    MkDos(p,root)
    while len(File)>0:
        pathDos = File.pop(0)
        p = max(0, p*np.exp(-t*Compteur))
        print(len(File))
        MkDos(p,pathDos)


#Enlever le commentaire de la ligne suivante et lancer la Fonction Boucle
#Boucle(0.9,0.000001)