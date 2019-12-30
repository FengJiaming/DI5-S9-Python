import cgi
import hashlib
from Cryptodome.Random import get_random_bytes

# Charger les informations utilisateur
users = []
with open('users.txt', 'rt') as fin:
    for line in fin.readlines():
        strUser = line.strip().split(';')
        name = strUser[0]
        password = strUser[1]
        users.append((name,password))

# Pour obtenir des informations sur le formulaire Web
form = cgi.FieldStorage()

username = form.getvalue("username")
password = form.getvalue("password")

html = """
<!DOCTYPE html>
    <head>
        <title>Mon programme</title>
    </head>
    <body>
        <h3>Page d'inscription</h3>
        <form action="/register.py" method="post">
            <label>Username : </label>
            <input type="text" name="username"/><br><br>
            <label>Password : </label>
            <input type="password" name="password"/><br><br>
            <input type="submit" name="send" value="S'inscrire">
        </form>"""

# Vérifiez si l'utilisateur existe déjà
def checkUsername(username):
    for user in users:
        if user[0] == username:
            return 1
    return 0

if username and password:
    if checkUsername(username):
        html += """<br><label>Ce nom utilisateur existe déjà!</label>"""
    else:
            # Stocker les informations utilisateur dans un fichier
            aesKey = get_random_bytes(16).hex()
            encryptedPassword = hashlib.sha256(aesKey.encode() + password.encode()).hexdigest() + ':' + aesKey
            usersFile = open('users.txt', 'at')
            usersFile.write(username + ";" + encryptedPassword + "\n")
            usersFile.close()
            users.append((username, encryptedPassword))
            html += """<br><label>Votre compte a bien été enregistré!</label>"""

html += """
                <br><br>
                <a href="index.py">Index</a>
            </body>
        </html>"""
print("Content-type: text/html; charset=utf-8\n")
print(html)
