import hashlib
import getpass
import random

command = '0'
cmd = "************************\n\
1.Inscription\n\
2.Connexion\n\
9.Quitter le programme\n\
************************\n\
Choisir la commande:\n"
filename = ""
while (command != '9'):
    command = input(cmd)
    if command == '1':
        login = input("Saisir votre login: ")
        password = getpass.getpass("Saisir votre mot de passe: ")
        salt = hashlib.sha512(str(random.random()).encode()).hexdigest()
        identifiant = login + '$' + salt
        mdp = hashlib.sha512(password.encode()).hexdigest()

        fic = open('bdd.txt','a')
        fic.write(identifiant + " " + mdp + "\n")
        fic.close

    if command == '2':
        login = input("Saisir votre login: ")
        password = getpass.getpass("Saisir votre mot de passe: ")
        mdp =  hashlib.sha512(password.encode()).hexdigest()
        fic = open('bdd.txt','r')

        while True:
            line = fic.readline()
            if line:
                line = line.strip('\n')
                tmpidf, tmpmdp = line.split(" ")
                tmplogin, tmpsalt = tmpidf.split("$")
                if (tmplogin==login) & (tmpmdp == mdp):
                    print("Connecte!")
                    break
            else:
                break
        if not line:
            print("Login ou Mdp Error!")
        fic.close
