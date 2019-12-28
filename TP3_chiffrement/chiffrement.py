'''
@author: Tianjiao & Jiaming
'''
from tkinter import *
from tkinter import messagebox
import hashlib

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

fields = 'UserName', 'Password'
stringSalage = 'FENG'
key_Password = ''


# Utiliser le « salage » pour renforcer le système avec une chaîne comprenant le login et une partie fixe.
def salage(login, password):
    mdp = stringSalage + password + login
    return hashlib.sha512(mdp.encode()).hexdigest()


# Obtenir les données d'entrée du champ de saisie
def fetch(entries):
    # Stocker le couple login et hash mot de passe dans un fichier texte.
    with open("data.txt", "a") as fic:
        for entry in entries:
            field = entry[0]
            text = entry[1].get()
            if field == "Password":
                password = text
            elif field == "UserName":
                login = text
        # Le nom d'utilisateur et le mot de passe sont stockés sur une ligne du fichier texte, séparés par un tab
        fic.write(login + "\t")
        fic.write(salage(login, password) + "\n")
        messagebox.showinfo("Success", "Les informations utilisateur sont stockées avec succès!")


# vérifier la présence d'un login et un mot de passe dans le fichier
def verify(entries, display_Key):
    with open("data.txt", "r") as fic:
        for line in fic.readlines():
            username = line.strip().split('\t')[0]
            password = line.strip().split('\t')[1]

            login = entries[0][1].get()
            password_In = entries[1][1].get()
            mdp = salage(login, entries[1][1].get())

            if login == username and mdp == password:
                global key_Password
                key_Password.set(password_In)
                messagebox.showinfo("Success", "Login success!")
                return 1
        messagebox.showerror("Error", "Le nom d'utilisateur ou le mot de passe est incorrect")


# Créer une interface de connexion, Renvoie les données saisies dans la zone de texte
def makeForm(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        if (field == 'Password'):
            ent['show'] = '*'
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    return entries


# Pour chiffrer un fichier avec un mot de passe
def encryptFile(filename, password):
    try:
        # Compléter la clé de cryptage sur 32 bits pour utiliser l'algorithme AES256
        key = pad(password.encode('utf-8'), AES.block_size * 2, style='pkcs7')
        cipher = AES.new(key, AES.MODE_EAX)
        with open(filename, mode='rb') as fic:
            data = fic.read()
            ciphertext, tag = cipher.encrypt_and_digest(data)
            fic.close()
        file_out = open("encrypted_" + filename, "wb")
        [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
        messagebox.showinfo("Success", "Crypté avec succès!")
    except Exception as e:
        messagebox.showerror("Error", e)

# Déchiffrer un fichier crypté avec un mot de passe
def decryptFile(filename, password):
    try:
        key = pad(password.encode('utf-8'), AES.block_size * 2, style='pkcs7')
        with open(filename, "rb") as file_in:
            nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
            cipher = AES.new(key, AES.MODE_EAX, nonce)
            data = cipher.decrypt_and_verify(ciphertext, tag)
            file_in.close()
        path = filename.strip().split('_')[1]
        with open("decrypted_" + path, "w") as fic:
            fic.write(str(data, encoding="utf-8"))
            fic.close()
    except Exception as e:
        messagebox.showerror("Error", e)
    else:
        messagebox.showinfo("Success", "Déchiffré avec succès")

# Créer un bouton "decrypt"
def decrypt(entries):
    if key_Password.get() != '':
        window_Decrypt = Tk()
        window_Decrypt.title("DecryptFile")
        filename = Entry(window_Decrypt, width=20)
        filename.grid(row=1, column=2)
        Label(window_Decrypt, text="Filename", width=15).grid(row=1, column=1)
        password = entries[1][1].get()
        Button(window_Decrypt, text='Decrypt', width=10, command=lambda: decryptFile(filename.get(), password)).grid(row=2, column=1)
    else:
        messagebox.showerror("Error", "Le mot de passe utilisé pour déchiffrer est vide! Veuillez vous connecter d'abord!")

# Créer un bouton "encrypt"
def encrypt():
    if key_Password.get() != '':
        window_Encrypt = Tk()
        window_Encrypt.title("EncryptFile")
        filename = Entry(window_Encrypt, width=20)
        filename.grid(row=1, column=2)
        Label(window_Encrypt, text="Filename", width=15).grid(row=1, column=1)
        # On utilise le mot de passe précédent pour chiffrer
        Button(window_Encrypt, text='Encrypt', width=10, command=lambda: encryptFile(filename.get(), key_Password.get())).grid(row=2, column=1)
    else:
        messagebox.showerror("Error", "Le mot de passe utilisé pour chiffrer est vide! Veuillez vous connecter d'abord!")

if __name__ == '__main__':
    root = Tk()
    root.title("UserInfo")

    ents = makeForm(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))

    Button(root, text='Sign Up', command=(lambda e=ents: fetch(e))).pack(side=LEFT, padx=5, pady=5)
    Button(root, text='Login', command=(lambda e=ents: verify(e, display_Key))).pack(side=LEFT, padx=5, pady=5)
    Button(root, text='Encrypt', command=encrypt).pack(side=LEFT, padx=5, pady=5)
    Button(root, text='Decrypt', command=(lambda e=ents: decrypt(e))).pack(side=LEFT, padx=5, pady=5)

    # Pour afficher le mot de passe pour le cryptage
    label_Key = Label(root, text="Key").pack(side=LEFT, padx=5, pady=5)
    key_Password = StringVar(value="")
    display_Key = Entry(root, textvariable = key_Password, state="readonly")
    display_Key.pack(side=LEFT, fill=X, padx=5, pady=5)

    root.mainloop()
