from Queue import Queue
from Stack import Stack
##Ej 10
noti1 = {'hora': '09:15', 'aplicacion': 'Facebook', 'mensaje': 'a .... le gustó tu foto'}
noti2 = {'hora': '11:43', 'aplicacion': 'Twitter', 'mensaje': ' @lola ha twitteado...'}
noti3 = {'hora': '11:43', 'aplicacion': 'Twitter', 'mensaje': ' @pepe ha twitteado "descubre el mundo de python..."'}
noti4 = {'hora': '13:00', 'aplicacion': 'Instagram', 'mensaje': 'te etiquetaron en una historia'}
noti5 = {'hora': '15:40', 'aplicacion': 'Facebook', 'mensaje': 'hoy cumple años tu amigo juan'}

cola_celular = Queue()


cola_celular.arrive(noti1)
cola_celular.arrive(noti2)
cola_celular.arrive(noti3)
cola_celular.arrive(noti4)
cola_celular.arrive(noti5)
def notificaciones_fb(cola: Queue) -> None:
    n = cola.size()
    for i in range(n):
        notificacion = cola.on_front()
        if notificacion['aplicacion'] == 'Facebook':
            cola.attention() #si es de fb lo elimina
        else:
            cola.move_to_end() #sino lo mueve al final

def notificaciones_tw(cola: Queue) -> None:
    n = cola.size()
    for i in range(n):
      notificacion = cola.on_front() #solo mira el primer elemento
      if notificacion['aplicacion'] == 'Twitter' and 'python' in notificacion['mensaje'].lower():
        print(notificacion['mensaje'])
      cola.move_to_end() #lo mueve al final

def filtrar(cola: Queue) -> int:
   contador = 0
   pila_temporal = Stack()
   for i in range(cola.size()):
    notificacion = cola.on_front() #miramos el frente
    if '11:43' <= notificacion['hora'] <= '15:57': #filtramos la hora
       pila_temporal.push(notificacion) #si cumple la condicion se guarda en la pila
       contador += 1
    cola.move_to_end()
   print(f'cantidad de notificaciones encontradas entre las 11:43 y las 15:57: {contador}')
   return contador
   
print('__Ejercicio 10____:')
print()
filtrar(cola_celular)
print()
notificaciones_tw(cola_celular)
print()
notificaciones_fb(cola_celular)
print()
cola_celular.show()

#EJ 16
def ej_16():
   cola_impresion = Queue()
   #a.
   cola_impresion.arribo_con_prioridad("Doc_empleado1",1)
   cola_impresion.arribo_con_prioridad("Doc_empleado2",1)
   cola_impresion.arribo_con_prioridad("Doc_empleado3",1)
   #b.
   prioridad, doc = cola_impresion.attention()
   print(f'imprimiendo: {doc}')
   #c.
   cola_impresion.arribo_con_prioridad("Doc_IT1",2)
   cola_impresion.arribo_con_prioridad("Doc_IT2",2)
   #D.
   cola_impresion.arribo_con_prioridad("Doc_gerente",3)
   #e.
   print('2 primeros documentos de la cola:')
   for i in range(2):
      print(f"-> {cola_impresion.attention()}")
   
   #f.
   cola_impresion.arribo_con_prioridad("empleado4",1)
   cola_impresion.arribo_con_prioridad("empleado5",1)
   cola_impresion.arribo_con_prioridad("gerente2",3)

   #g.
   print('imprimiendo todos los documentos de la cola:')
   while cola_impresion.size() > 0:
       print(f"-> {cola_impresion.attention()}")
print('__Ejercicio 16____:')
ej_16()  
print()
#EJ 22
cola_mcu = Queue()

cola_mcu.arrive({'nombre': 'Tony Stark', 'superheroe': 'Iron Man', 'género': 'm'})
cola_mcu.arrive({'nombre': 'Wanda Maximoff', 'superheroe': 'Scarlet Witch', 'género': 'f'})
cola_mcu.arrive({'nombre': 'Scott Lang', 'superheroe': 'Ant-Man', 'género': 'm'})
cola_mcu.arrive({'nombre': 'Steve Rogers', 'superheroe': 'Capitán América', 'género': 'm'})
cola_mcu.arrive({'nombre': 'Natasha Romanoff', 'superheroe': 'Black Widow', 'género': 'f'})
cola_mcu.arrive({'nombre': 'Carol Danvers', 'superheroe': 'Capitana Marvel', 'género': 'f'})
cola_mcu.arrive({'nombre': 'Clinton Barton', 'superheroe': 'Hawkeye','género': 'm'})

def nombre_capitana(cola:Queue)-> str:
   for i in range(cola.size()):
      personaje = cola.on_front()
      if personaje['superheroe'].lower() == 'capitana marvel':
         print(f'El nombre del personaje de Capitana Marvel es: {personaje["nombre"]}')
      cola.move_to_end()

def superheroes_f(cola: Queue)-> None:
    print("-----superheroes femeninos-----:")
    for i in range(cola.size()):
        personaje = cola.on_front()
        if personaje['género'].lower() == 'f':
            print(f'Nombre:{personaje["superheroe"]}')
        cola.move_to_end()

def superheroes_m(cola: Queue)-> None:
    print("-----superheroes masculinos-----:")
    for i in range(cola.size()):
        personaje = cola.on_front()
        if personaje['género'].lower() == 'm':
            print(f'Nombre:{personaje["superheroe"]}')
        cola.move_to_end()

def nombre_scott(cola:Queue)-> str:
   for i in range(cola.size()):
      personaje = cola.on_front()
      if personaje['nombre'].lower() == 'scott lang':
         print(f'El nombre de superhero de Scott Lang es: {personaje["superheroe"]}')
      cola.move_to_end()

def con_s(cola:Queue)-> None:
   print('personajes con la letra s:')
   for i in range(cola.size()):
      personaje = cola.on_front()
      nombre_real = personaje['nombre'].upper().startswith('S')
      nombre_heroe = personaje['superheroe'].upper().startswith('S')
      if nombre_real or nombre_heroe:
         print(f"Personaje:{personaje['nombre']}// Heroe:{personaje['superheroe']}")
      cola.move_to_end()

def nombre_carol(cola: Queue) -> None:
   encontrado = False
   for i in range(cola.size()):
      personaje = cola.on_front()
      if personaje['nombre'].lower() == 'carol danvers':
         print(f"Carol danvers ha sido encontrada, su nombre de heroe es: ({personaje['superheroe']})")
         encontrado = True
      cola.move_to_end()
   if not encontrado:
      print('Carol Danvers no se encuentra en la cola.')
print()
print('__Ejercicio 22___:')
print()
nombre_capitana(cola_mcu)
print()
superheroes_f(cola_mcu)
superheroes_m(cola_mcu)
print() 
nombre_scott(cola_mcu)
print()
con_s(cola_mcu)
print()
nombre_carol(cola_mcu)

