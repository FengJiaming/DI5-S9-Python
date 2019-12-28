# -*- coding: utf-8 -*-

from tkinter import *

import tkinter as tk
from  tkinter import messagebox

#Il doit importer la bibliothèque math pour pouvoir utiliser des fonctions telles que tan, sin, cos.,
import math
from math import *

from functools import partial

# Recevoir la valeur saisie par la calculatrice à afficher dans la zone de saisie
def get_input(entry, argu):
    if entry.get() == "0" and argu in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", "tan(", "sin(", "cos("]:
        text.set(argu)
    elif entry.get()[-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")"] and argu in ["(", "tan(", "sin(", "cos("]:
        argu = "*" + argu
        text.set(text.get() + argu)
    elif entry.get() == "Erreur syntaxe":
        text.set(argu)
    else:
        text.set(text.get() + argu)

# C: efface la dernière touche cliquée
def backspace(entry):
    input_len = len(entry.get())
    if input_len > 1:
        text.set(entry.get()[:-1])
    else:
        text.set("0")

# AC:efface toutes les touches bufferisées
def clear():
    text.set("0")

#évaluer l'expression à l'aide de la fonction eval
def calc(entry):
    try:
        input = entry.get()
        output = str(eval(input.strip())) #
        text.set(output)
    except SyntaxError:
        text.set("Erreur syntaxe")
    except NameError:
        text.set("Erreur syntaxe")
    except TypeError:
        text.set("Erreur syntaxe")
    except ZeroDivisionError:
        text.set("Erreur syntaxe")

# √ Racine carrée
def squareroot(entry):
    try:
        input = entry.get()
        value = eval(input.strip())  #
    except SyntaxError:
        text.set("Erreur syntaxe")
    except NameError:
        text.set("Erreur syntaxe")
    except TypeError:
        text.set("Erreur syntaxe")
    except ZeroDivisionError:
        text.set("Erreur syntaxe")
    else:
        output = math.sqrt(value)
        text.set(output)

# x² Carré
def square(entry):
    try:
        input = entry.get()
        value = eval(input.strip())
    except SyntaxError:
        text.set("Erreur syntaxe")
    except NameError:
        text.set("Erreur syntaxe")
    except TypeError:
        text.set("Erreur syntaxe")
    except ZeroDivisionError:
        text.set("Erreur syntaxe")
    else:
        output = math.pow(value, 2)
        text.set(output)

# x! factorielle
def factorielle(entry):
    try:
        input = entry.get()
        value = eval(input.strip())
    except SyntaxError:
        text.set("Erreur syntaxe")
    except NameError:
        text.set("Erreur syntaxe")
    except TypeError:
        text.set("Erreur syntaxe")
    except ZeroDivisionError:
        text.set("Erreur syntaxe")
    else:
        output = math.factorial(value)
        text.set(output)

# mode basique
def Basique(entry):
    for button in scientific_buttons:
        button.destroy()
    entry.grid(columnspan=4)

# mode scientifique
def Scientifique(entry):
    global scientific_buttons

    myButton = partial(Button,  bg='#D5E0EE', width=7, height=2, font=("Arial", 15), activebackground='#4F4F4F')
    buttonSin=myButton(text='sin', command=lambda: get_input(entry, 'sin('))
    buttonSin.grid(row=2, column=4, sticky=N + S + E + W)
    buttonCos = myButton( text='cos', command=lambda: get_input(entry, 'cos('))
    buttonCos.grid(row=3, column=4, sticky=N + S + E + W)
    buttonTan = myButton( text='tan', command=lambda: get_input(entry, 'tan('))
    buttonTan.grid(row=4, column=4, sticky=N + S + E + W)
    buttonX = myButton( text='x!', command=lambda: factorielle(entry))
    buttonX.grid(row=1, column=4, sticky=N + S + E + W)
    buttonSqrt = myButton( text='√', command=lambda: squareroot(entry))
    buttonSqrt.grid(row=5, column=4, sticky=N + S + E + W)
    buttonPow = myButton( text='x²', command=lambda: square(entry))
    buttonPow.grid(row=6, column=4, sticky=N + S + E + W)

    scientific_buttons.append(buttonSin)
    scientific_buttons.append(buttonCos)
    scientific_buttons.append(buttonTan)
    scientific_buttons.append(buttonX)
    scientific_buttons.append(buttonSqrt)
    scientific_buttons.append(buttonPow)

    entry.grid(columnspan=5)

def About(root):
    print("@Author: Tianjiao XU & Jiaming FENG")
    tk.messagebox.showinfo(title='About', message='@Author: Tianjiao XU & Jiaming FENG')

def calculatrice():
    # Initialiser la fenêtre
    root = Tk()
    root.title("Calculatrice")
    root.resizable(width= False, height=False)

    # Créer une zone de saisie
    global  text
    text = StringVar(value="0")

    entry = Entry(root, textvariable=text, justify="right", font=("Arial", 28), state="readonly")
    entry.grid(row=0, column=0, columnspan=4, sticky=N + W + S + E, padx=5, pady=5)

    # ajouter des boutons
    button_bg = '#D5E0EE'
    button_active_bg = '#4F4F4F'

    myButton = partial(Button, root, bg=button_bg, width=7, height=2, font=("Arial", 15), activebackground=button_active_bg)
    myButton(text='(', command=lambda: get_input(entry, '(')).grid(row=1, column=0, columnspan=2, sticky=N + S + E + W)
    myButton(text=')', command=lambda: get_input(entry, ')')).grid(row=1, column=2, columnspan=2, sticky=N + S + E + W)
    myButton(text='7', command=lambda: get_input(entry, '7')).grid(row=2, column=0, sticky=N + S + E + W)
    myButton(text='8', command=lambda: get_input(entry, '8')).grid(row=2, column=1, sticky=N + S + E + W)
    myButton(text='9', command=lambda: get_input(entry, '9')).grid(row=2, column=2, sticky=N + S + E + W)
    myButton(text='+', command=lambda: get_input(entry, '+')).grid(row=2, column=3, sticky=N + S + E + W)
    myButton(text='4', command=lambda: get_input(entry, '4')).grid(row=3, column=0, sticky=N + S + E + W)
    myButton(text='5', command=lambda: get_input(entry, '5')).grid(row=3, column=1, sticky=N + S + E + W)
    myButton(text='6', command=lambda: get_input(entry, '6')).grid(row=3, column=2, sticky=N + S + E + W)
    myButton(text='-', command=lambda: get_input(entry, '-')).grid(row=3, column=3, sticky=N + S + E + W)
    myButton(text='1', command=lambda: get_input(entry, '1')).grid(row=4, column=0, sticky=N + S + E + W)
    myButton(text='2', command=lambda: get_input(entry, '2')).grid(row=4, column=1, sticky=N + S + E + W)
    myButton(text='3', command=lambda: get_input(entry, '3')).grid(row=4, column=2, sticky=N + S + E + W)
    myButton(text='*', command=lambda: get_input(entry, '*')).grid(row=4, column=3, sticky=N + S + E + W)
    myButton(text='0', command=lambda: get_input(entry, '0')).grid(row=5, column=0, columnspan=2, sticky=N + S + E + W)
    myButton(text='.', command=lambda: get_input(entry, '.')).grid(row=5, column=2, sticky=N + S + E + W)

    myButton(text='/', command=lambda: get_input(entry, '/')).grid(row=5, column=3, sticky=N + S + E + W)
    myButton(text='AC', command=lambda: clear()).grid(row=6, column=0, sticky=N + S + E + W)
    myButton(text='C', command=lambda: backspace(entry)).grid(row=6, column=1, sticky=N + S + E + W)
    myButton(text='=', command=lambda: calc(entry)).grid(row=6, column=2, columnspan=2, sticky=N + S + E + W)

    # Ajouter la barre de menu
    menu = Menu(root)
    root.config(menu=menu)
    modeMenu = Menu(menu)
    menu.add_cascade(label="Mode", menu=modeMenu)
    modeMenu.add_command(label="Basique", command=lambda:Basique(entry))
    modeMenu.add_command(label="Scientifique", command=lambda:Scientifique(entry))

    modeMenu.add_separator()
    modeMenu.add_command(label="Exit", command=root.quit)

    helpmenu = Menu(menu)
    menu.add_cascade(label="Aide", menu=helpmenu)
    helpmenu.add_command(label="About...", command=lambda : About(root))

    root.mainloop()


if __name__ == '__main__':
    scientific_buttons = []
    calculatrice()



