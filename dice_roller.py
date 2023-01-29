# Python Programming : GUI Applications 
# Ejemplo de uso del tkinter                                
# Lanza los dados
from tkinter import *
from random import randint

App = Tk()
App.title("Lanza los dados")
App.geometry("250x250")

# Diccionario de caracteres unicode para los dados
Dice = {
    0 : '?',
    1 : '⚀',
    2 : '⚁',
    3 : '⚂',
    4 : '⚃',
    5 : '⚄',
    6 : '⚅'
}
# Creación del frame
app_frame = Frame(App)
app_frame.pack(pady= 20)

# Primer  caracter de los dados cuando la aplicación comienza

dice_lbl_1 = Label(app_frame, text=Dice[0], font=('Helvatica', 100))
dice_lbl_1.grid(row=0, column=0, padx=5)

dice_lbl_2 = Label(app_frame, text=Dice[0], font=('Helvatica', 100))
dice_lbl_2.grid(row=0, column=1, padx=5)

# Elige un número entre 1 y 6 aleatoriamente para cada dado y los muestra en pantalla.
def roll():
 
    dice_choice_1 = randint(1, 6)
    dice_choice_2 = randint(1, 6)
  
    dice_lbl_1.config(text=Dice[dice_choice_1], font=('Helvatica', 100))
    dice_lbl_1.grid(row=0, column=0, padx=5)
    dice_lbl_2.config(text=Dice[dice_choice_2], font=('Helvatica', 100))
    dice_lbl_2.grid(row=0, column=1, padx=5)

# Crear botón roll_button
roll_button = Button(App, text='Roll', command=roll)
roll_button. pack(pady=20)

App.mainloop()