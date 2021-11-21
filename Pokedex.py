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
from PyQt5.QtWidgets import QAbstractItemView, QMainWindow, QApplication, QTableWidgetItem
import sys

window = tk.Tk()
window.geometry('600x500')
window.title('Pokédex')
window.config(padx=10,pady=10)

titulo = tk.Label(window, text='Pokédex')
titulo.config(font=('Arial',32))
titulo.pack(padx=10,pady=10)

class index(QMainWindow):
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

    def __init__(self):
        super().__init__()
        uic.loadUi("./view/menu.ui", self)
        for i in range(1,totalPoke):
            if i < 152:
                self.pokemons['gen1'].append(str(i))
            if i >= 152 and i <= 251:
                self.pokemons['gen2'].append(str(i))
            if i >= 252 and i <= 386:
                self.pokemons['gen3'].append(str(i))
            if i >= 387 and i <= 493:
                self.pokemons['gen4'].append(str(i))
            if i >= 494 and i <= 649:
                self.pokemons['gen5'].append(str(i))
            if i >= 650 and i <= 721:
                self.pokemons['gen6'].append(str(i))
            if i >= 722 and i <= 809:
                self.pokemons['gen7'].append(str(i))
            if i >= 810 and i <= 898:
                self.pokemons['gen8'].append(str(i))
                
        self.gen1Button.clicked.connect(lambda:self.ventana2('1'))
        self.gen2Button.clicked.connect(lambda:self.ventana2('2'))
        self.gen3Button.clicked.connect(lambda:self.ventana2('3'))
        self.gen4Button.clicked.connect(lambda:self.ventana2('4'))
        self.gen5Button.clicked.connect(lambda:self.ventana2('5'))
        self.gen6Button.clicked.connect(lambda:self.ventana2('6'))
        self.gen7Button.clicked.connect(lambda:self.ventana2('7'))
        self.gen8Button.clicked.connect(lambda:self.ventana2('8'))

        
    
    def ventana2(self,gen):
        self.ventana=QtWidgets.QMainWindow()
        uic.loadUi("./view/tabla.ui", self)
        self.numGen.setText(str(gen))
        self.regresar.clicked.connect(self.regresar2)
        #Poke = lista de pokemones de la generacion seleccionada
        poke = self.multiDescarga(self.pokemons['gen'+str(gen)])
        self.tabla.setRowCount(len(poke))
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.setDragDropOverwriteMode(False)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        for i in range(0,len(poke)):
            name = poke[i].name.capitalize()
            self.tabla.setItem(i,0,QTableWidgetItem(name))
            text = '-'.join([t for t in poke[i].types])
            text = text.replace('normal','Normal').replace('steel','Acero').replace('water','Agua').replace('bug','Bicho').replace('dragon','Dragón').replace('electric','Electrico').replace('ghost','Fantasma').replace('fire','Fuego').replace('fairy','Hada').replace('ice','Hielo').replace('fighting','Lucha').replace('grass','Planta').replace('psychic','Psiquico').replace('dark','Siniestro').replace('ground','Tierra').replace('poison','Veneno').replace('flying','Volador').replace('rock','Roca')
            self.tabla.setItem(i,1,QTableWidgetItem(text))
      
    def regresar2(self):
        uic.loadUi("./view/menu.ui", self)
        self.gen1Button.clicked.connect(lambda:self.ventana2('1'))
        self.gen2Button.clicked.connect(lambda:self.ventana2('2'))
        self.gen3Button.clicked.connect(lambda:self.ventana2('3'))
        self.gen4Button.clicked.connect(lambda:self.ventana2('4'))
        self.gen5Button.clicked.connect(lambda:self.ventana2('5'))
        self.gen6Button.clicked.connect(lambda:self.ventana2('6'))
        self.gen7Button.clicked.connect(lambda:self.ventana2('7'))
        self.gen8Button.clicked.connect(lambda:self.ventana2('8'))

    def buscarPokemon(self,id):
        pokemon = pypokedex.get(name=id)
        print(pokemon)
        return pokemon

    def multiDescarga(self,limitePokemones):
        print('Procesos')
        with ThreadPoolExecutor(max_workers=len(limitePokemones)) as executor:
            return list(executor.map(self.buscarPokemon,limitePokemones))    



totalPoke = 900


    
def vista():
    app = QApplication(sys.argv)
    GUI = index()
    GUI.show()
    
    sys.exit(app.exec_())
    


      
#    with Pool(len(limitePokemones)) as p:
#       return p.map(buscarPokemon,limitePokemones) 
      
#       for i in range(len(hola)):
#           pokemones.append(hola[i])
#       p.terminate()
#    print('Termine')
#    breakpoint
    

if __name__ == '__main__':

    print('Inicio')

    # for i in range(8):
    #     pokemones.append(multiDescarga(pokemons['gen'+str(i+1)]))
    

    vista()
    # thread = Thread(target=multiDescarga, args=(pokemons['gen1'],))
    # thread.start()
    # return_value = thread.join()
    # print(return_value)
    # pokemones = multiHilos()
    # print(pokemones[1].dex)




    



# window.mainloop()