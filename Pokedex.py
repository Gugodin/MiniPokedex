from concurrent.futures.thread import ThreadPoolExecutor
import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO
from multiprocessing import Pool
from threading import Thread
from urllib3 import response
import time


window = tk.Tk()
window.geometry('600x500')
window.title('Pokédex')
window.config(padx=10,pady=10)

titulo = tk.Label(window, text='Pokédex')
titulo.config(font=('Arial',32))
titulo.pack(padx=10,pady=10)

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
    

def isSorted(array:list):
    for i in range(len(array)):
        if i+1 < len(array):
            if array[i] > array[i+1]:
                return False
    return True

def sortPokemons(array:list):
    i = 0
    while True:
        if array[i] > array[i+1]:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
            i = i - 1
        else:
            i = i + 1
        if isSorted(array):
            return array
            

def multiDescarga(limitePokemones):
   print('Procesos')
   with ThreadPoolExecutor(max_workers=len(limitePokemones)) as executor:
    return list(executor.map(buscarPokemon,limitePokemones))


if __name__ == '__main__':
    
    print('Inicio')

    # for i in range(8):
    #     pokemones.append(multiDescarga(pokemons['gen'+str(i+1)]))
    
    # print(len(pokemones))
    # thread = Thread(target=multiDescarga, args=(pokemons['gen1'],))
    # thread.start()
    # return_value = thread.join()
    # print(return_value)
    # pokemones = multiHilos()
    # print(pokemones[1].dex)


# window.mainloop()
