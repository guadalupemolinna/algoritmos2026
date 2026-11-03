from graph import Graph

personajes = {
    'Luke Skywalker': {3, 4, 5, 6, 7, 8, 9},
    'Darth Vader': {3, 4, 5, 6},
    'Yoda': {1, 2, 3, 5, 6, 8},
    'Boba Fett': {2, 5, 6},
    'C-3PO': set(range(1, 10)),
    'Leia': {3, 4, 5, 6, 7, 8, 9},
    'Rey': {7, 8, 9},
    'Kylo Ren': {7, 8, 9},
    'Chewbacca': {3, 4, 5, 6, 7, 8, 9},
    'Han Solo': {4, 5, 6, 7, 9},
    'R2-D2': set(range(1, 10)),
    'BB-8': {7, 8, 9},
}

grafo = Graph(is_dir=False)

for nombre, episodios in personajes.items():
    grafo.add_vertex(nombre, episodios)

nombres = list(personajes)
for i in range(len(nombres)):
    for j in range(i + 1, len(nombres)):
        juntos = len(personajes[nombres[i]] & personajes[nombres[j]])
        if juntos > 0:
            grafo.add_edge(juntos, nombres[i], nombres[j])

print(f'personajes cargados: {grafo.size()}')



for inicio in ['C-3PO', 'Yoda', 'Leia']:
    aristas = grafo.kruskal(inicio)
    print(f'\narbol de expansion minimo desde {inicio}')
    peso_total = 0
    for origen, destino, peso in aristas:
        print(f'{origen} - {destino} ({peso})')
        peso_total += peso
    print(f'aristas: {len(aristas)} -- peso total: {peso_total}')


maximo = 0
pares = []
for vertex in grafo:
    for edge in vertex.edges:
        if vertex.value < edge.destination:
            if edge.weight > maximo:
                maximo = edge.weight
                pares = [(vertex.value, edge.destination)]
            elif edge.weight == maximo:
                pares.append((vertex.value, edge.destination))

print(f'\nmaximo de episodios compartidos: {maximo}')
for a, b in pares:
    print(f'{a} y {b}')

def camino_corto(grafo, origen, destino):
    if not grafo.exist_path(origen, destino):
        return None, None

    pila = grafo.dijkstra(origen)
    camino = []
    costo = None
    buscado = destino
    while pila.size() > 0:
        valor = pila.pop()    
        if valor[0] == buscado:
            if costo is None:
                costo = valor[1]
            camino.append(valor[0])
            buscado = valor[2]
    camino.reverse()
    return camino, costo
for origen, destino in [('C-3PO', 'R2-D2'), ('Yoda', 'Darth Vader')]:
    camino, costo = camino_corto(grafo, origen, destino)
    print(f'\ncamino mas corto de {origen} a {destino}')
    if camino is None:
        print('no existe camino')
    else:
        print(f'{" -> ".join(camino)} | costo: {costo}')

print('\npersonajes presentes en los 9 episodios')
for vertex in grafo:
    if len(vertex.other_values) == 9:
        print(vertex.value)