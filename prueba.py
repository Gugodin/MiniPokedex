from concurrent.futures.thread import ThreadPoolExecutor
from PyQt5 import QtWidgets
import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO
from multiprocessing import Pool
from threading import Thread
from urllib3 import response
import time
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

window = tk.Tk()
window.geometry('600x500')
window.title('Pokédex')
window.config(padx=10,pady=10)

titulo = tk.Label(window, text='Pokédex')
titulo.config(font=('Arial',32))
titulo.pack(padx=10,pady=10)

class index(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("vista.ui", self)
        self.gen1Button.clicked.connect(self.ventana2)
    
    def ventana2(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=uic.loadUi("vistas.ui", self)
    


def buscarPokemon(id):
    pokemon = pypokedex.get(name=id)
    print(pokemon)
    return pokemon
    


    

pokemons = {
    'gen1' : [],
    'gen2' : [],
    'gen3' : [],
    'gen4' : [],
    'gen5' : [],
    'gen6' : [],
    'gen7' : [],
    'gen8' : []
}

totalPoke = 900

for i in range(1,totalPoke):
    if i < 152:
        pokemons['gen1'].append(str(i))
    if i >= 152 and i <= 251:
        pokemons['gen2'].append(str(i))
    if i >= 252 and i <= 386:
        pokemons['gen3'].append(str(i))
    if i >= 387 and i <= 493:
        pokemons['gen4'].append(str(i))
    if i >= 494 and i <= 649:
        pokemons['gen5'].append(str(i))
    if i >= 650 and i <= 721:
        pokemons['gen6'].append(str(i))
    if i >= 722 and i <= 809:
        pokemons['gen7'].append(str(i))
    if i >= 810 and i <= 898:
        pokemons['gen8'].append(str(i))
    
def vista():
    app = QApplication(sys.argv)
    GUI = index()
    GUI.show()
    
    sys.exit(app.exec_())
    

def multiDescarga(limitePokemones):
   print('Procesos')
   with ThreadPoolExecutor(max_workers=len(limitePokemones)) as executor:
    return list(executor.map(buscarPokemon,limitePokemones))
      
#    with Pool(len(limitePokemones)) as p:
#       return p.map(buscarPokemon,limitePokemones) 
      
#       for i in range(len(hola)):
#           pokemones.append(hola[i])
#       p.terminate()
#    print('Termine')
#    breakpoint
    

if __name__ == '__main__':
    
    genracion1 =None
    print('Inicio')

    pokemones = []

    for i in range(8):
        pokemones.append(multiDescarga(pokemons['gen'+str(i+1)]))
    
    print(len(pokemones))

    vista()
    # thread = Thread(target=multiDescarga, args=(pokemons['gen1'],))
    # thread.start()
    # return_value = thread.join()
    # print(return_value)
    # pokemones = multiHilos()
    # print(pokemones[1].dex)




    



# window.mainloop()