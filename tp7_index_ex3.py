import cgi

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")
print(form.getvalue("name"))
fic = open("tp7_ex3_data",'a')
text = form.getvalue("name")
if text != None:
    fic.write(text + "\n")
fic.close
html = """<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<body>
    <form action="/tp7_index_ex3.py" method="post">
        <input type="text" name="name" value="Votre nom" />
        <input type="submit" name="send" value="Envoyer information au serveur">
    </form>
</body>
</html>
"""
print(html)
