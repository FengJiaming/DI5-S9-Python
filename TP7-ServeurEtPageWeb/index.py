#!/usr/bin/python3
import cgi
import hashlib

# Pour obtenir des informations sur le formulaire Web
form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

username = form.getvalue("username")
password = form.getvalue("password")
logout = form.getvalue("logout")

if logout:
    user = ""
    username = ""
    password = ""

# Charger les informations utilisateur
users = []
with open('users.txt', 'rt') as fin:
   for line in fin.readlines():
       strUser = line.strip().split(';')
       name = strUser[0]
       pwd = strUser[1]
       users.append((name,pwd))

# La fonction pour Vérifier la connexion
def connect(username, password):
    for user in users:
        if user[0] == username:
            encryptedUserPassword, salt = user[1].split(':')
            encryptedPassword = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
            if encryptedUserPassword == encryptedPassword:
                return user
            else:
                return 0
        else:
            return 0

# Page principale lorsque vous n'êtes pas connecté
html = """<!DOCTYPE html>
<head>
   <title>Mon programme</title>
</head>
<body>
   <h3>Index</h3>
   <form action="/index.py" method="post">
       <label>Username</label>
       <input type="text" name="username"/><br><br>
       <label>Password</label>
       <input type="password" name="password"/><br><br>
   <input type="submit" name="send" value="Se connecter">
   </form>"""

# Interface de traitement de connexion
if username and password:
    user = connect(username, password)
    if user == 0:
        html += """<br><label>Nom d'utilisateur ou mot de passe incorrect</label>"""
    else:
        html = """
            <!DOCTYPE html>
                <head>
                    <title>Mon programme</title>
                </head>
                <body>
                    <h3>User page</h3>
                    <label>""" + user[0] + """</label><br><br>
                    <form action="/index.py" method="post">
                        <input type="hidden" name="logout" value="true">
                        <input type="submit" name="send" value="Logout">
                    </form>
                </body>
            </html>"""
        print(html)
        exit(0)

# Interface d'inscription
html += """
           <br><br>
           <a href="register.py">S'inscrire</a>
       </body>
   </html>"""

print(html)

