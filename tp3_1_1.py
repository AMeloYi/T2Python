command = '0'
str = "************************\n\
1.Choisir un num de fichier\n\
2.Ajouter un texte\n\
3.Afficher le fichier complet\n\
4.Vider le fichier\n\
9.Quitter le programme\n\
************************\n\
Choisir la commande:\n"
filename = ""
while (command != '9'):
    command = input(str)
    if command == '1':
        filename = input("Choisir le nom de fichier:\n")
        print ("Fichier choisi : " + filename)
        try:
            fic = open(filename,'r')
        except IOError:
            print("Ne peut ecrire le fichier ou le fichier n'existe pas")
        else:
            fic.close
    if command == '2':
        if filename == "":
            print ("Choisir un fichier svp!\n")
            continue
        try:
            fic = open(filename,'a')
            text = input("Saisir un texte dans la fichier : ")
            fic.write(text)
        except IOError:
            print("Ne peut ecrire le fichier ou le fichier n'existe pas")
        else:
            print ("La texte est ajoute!")
            fic.close
    if command == '3':
        if filename == "":
            print ("Choisir un fichier svp!\n")
            continue
        try:
            print ("Afficher le fichier :")
            with open(filename,'r') as fic:
                print(fic.read())
        except IOError:
            print("Ne peut ecrire le fichier ou le fichier n'existe pas")
        else:
            fic.close
    if command == '4':
        if filename == "":
            print ("Choisir un fichier svp!\n")
            continue
        try:
            fic = open(filename,'w')
            fic.truncate()
        except IOError:
            print("Ne peut ecrire le fichier ou le fichier n'existe pas")
        else:
            print ("Le fichier est vide!")
            fic.close
