import cgi
count = 0
form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")
html = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<body>
    <form action="/tp7_index_ex4.py" method="post">
        <input type="text" name="login" value="login" />
        <input type="text" name="mdp" value="mdp" />
        <input type="submit" name="send" value="Envoyer information au serveur">
    </form>
</body>
</html>
"""
print(html)
fic = open("tp7_ex4_data",'r')
login = form.getvalue("login")
mdp = form.getvalue("mdp")
while True:
    line = fic.readline()
    if line:
        line = line.strip('\n')
        tmplogin, tmpmdp = line.split(" ")
        if (tmplogin==login) & (tmpmdp == mdp):
            print("Connecte!")
            break
    else:
        break
if not line:
    print("Login ou Mdp Error!")
fic.close
