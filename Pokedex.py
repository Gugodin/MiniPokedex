from concurrent.futures.thread import ThreadPoolExecutor
from PyQt5 import QtWidgets
import pypokedex
import urllib3
from io import BytesIO
from multiprocessing import Pool
from threading import Thread
from urllib3 import response
from PyQt5 import uic
from PyQt5.QtWidgets import QAbstractItemView, QMainWindow, QApplication, QTableWidgetItem, QDialog
import sys
from PyQt5.QtGui import QPixmap
import PIL.Image, PIL.ImageQt


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
        #self.setStyleSheet("background-color: gray;")
        for i in range(1,900):
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
        self.datos.clicked.connect(lambda:self.ventana3(self.tabla.currentItem().row()))
        
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

    def ventana3(self,name2):
        print('boton3')
        name = str(self.tabla.item(name2,0).text())
        name = name.lower()
        pokemon = self.buscarPokemon(name)
        tipo = '-'.join([t for t in pokemon.types])
        tipo = tipo.replace('normal','Normal').replace('steel','Acero').replace('water','Agua').replace('bug','Bicho').replace('dragon','Dragón').replace('electric','Electrico').replace('ghost','Fantasma').replace('fire','Fuego').replace('fairy','Hada').replace('ice','Hielo').replace('fighting','Lucha').replace('grass','Planta').replace('psychic','Psiquico').replace('dark','Siniestro').replace('ground','Tierra').replace('poison','Veneno').replace('flying','Volador').replace('rock','Roca')
        
        print(name+' '+ tipo)

        http= urllib3.PoolManager()
        response = http.request('GET', pokemon.sprites.front.get('default'))
        
        image = PIL.Image.open(BytesIO(response.data))

        img = PIL.ImageQt.toqpixmap(image)

        # qpixmap = QPixmap(img)

        self.poke = pokemonWindow(name,tipo,pokemon.dex,img)
        self.poke.exec_()




    def buscarPokemon(self,id):
        pokemon = pypokedex.get(name=id)
        print(pokemon)
        return pokemon

    def multiDescarga(self,limitePokemones):
        print('Procesos')
        with ThreadPoolExecutor(max_workers=len(limitePokemones)) as executor:
            return list(executor.map(self.buscarPokemon,limitePokemones))    



class pokemonWindow(QDialog):
    def __init__(self,pokemonName:str,pokemonType:str,pokemonIndex:str,image):
        QDialog.__init__(self)
        uic.loadUi('./view/pokemon.ui',self)
        self.nombreP.setText(pokemonName.capitalize())
        self.tipos.setText(str(pokemonType))
        self.numero.setText(str(pokemonIndex))
        self.sprite.setPixmap(image)


def vista():
    app = QApplication(sys.argv)
    GUI = index()
    GUI.show()
    
    sys.exit(app.exec_())
    
    

if __name__ == '__main__':

    vista()





    


