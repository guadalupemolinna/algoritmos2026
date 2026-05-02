#EJ 20#
from stack import Stack
pila_mov = Stack()

respuesta = input('desea registrar un movimiento? s/n:').lower()

while respuesta == 's':
    pasos = int(input('ingrese cantidad dde pasos: '))
    direccion = input('ingrese dirección:').lower()
    pila_mov.push((pasos, direccion))
    respuesta = input('desea continuar registrando movimientos? s/n').lower()


print('generando camino de regreso')
while pila_mov.size() > 0:
    pasos, direccion = pila_mov.pop()
    if direccion == 'norte':
        direccion = 'sur'
    elif direccion == 'sur':
        direccion = 'norte'
    elif direccion == 'este':
        direccion = 'oeste'
    elif direccion == 'oeste':
        direccion = 'este'
    elif direccion == 'noreste':
        direccion = 'suroeste'
    elif direccion == 'suroeste':
        direccion = 'noreste'
    elif direccion == 'noroeste':
        direccion = 'sureste'
    elif direccion == 'sureste':
        direccion = 'noroeste'

    print(f'{pasos} pasos hacia {direccion}')

#EJ 24
from stack import Stack
pila_pers = Stack()

personajes = [
    ('Iron Man', 10),
    ('Black Widow',8),
    ('Spider-Man',5),
    ('Rocket',6),
    ('Groot',5),
    ('Capitan America',9),
    ('Doctor Strange',6)
]

for nombre, peli in personajes:
    pila_pers.push([nombre, peli])

def resolver_mcu(pila):
    pila_aux = Stack()
    pos = 1

    pos_rocket = None
    pos_groot = None
    personajes_5 = []
    pelis_black = 0
    personajes_cdg = []

    while pila.size() > 0:
      personaje = pila.pop()

    #a. posiciones de rocket y groot
      if personaje[0] == 'Rocket':
        pos_rocket = pos
      if personaje[0] == 'Groot':
        pos_groot = pos
    #b. personajes que participan en mas de 5 pelis y cantidad de pelis en la que aparecen
      if personaje[1] > 5:
        personajes_5.append(personaje)
     #c. determinar en cuantas peliculas aparece black widow
      if personaje[0] == 'Black Widow':
        pelis_black = personaje[1]
        #d. mostrar todos los personajes cuyo nombre empieza con c, d y g
      if personaje[0][0].upper() in ['C', 'D', 'G']:
         personajes_cdg.append(personaje[0])

      pila_aux.push(personaje)
      pos += 1
      #se devuelve todo a la pila original
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

    
    print(f"Rocket está en la pos: {pos_rocket}, Groot en la pos: {pos_groot}")
    print(f"Personajes con mas de5 pelis: {personajes_5}")
    print(f"Black Widow estuvo en {pelis_black} películas")
    print(f"Personajes con C, D o G: {personajes_cdg}")

#llamada a la función
resolver__mcu(pila_pers)
