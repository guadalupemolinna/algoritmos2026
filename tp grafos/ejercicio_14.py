"ejercicio 14 - Ambientes de una casa (grafo no dirigido, pesos en metros)"
from graph import Graph

AMBIENTES = ['cocina', 'comedor', 'cochera', 'quincho', 'baño 1', 'baño 2',
             'habitación 1', 'habitación 2', 'sala de estar', 'terraza', 'patio']

# (metros, origen, destino)
PASILLOS = [
    (4, 'cocina', 'comedor'), (9, 'cocina', 'cochera'), (8, 'cocina', 'quincho'),
    (5, 'cocina', 'patio'), (7, 'cocina', 'sala de estar'),
    (3, 'comedor', 'sala de estar'), (6, 'comedor', 'baño 1'),
    (10, 'comedor', 'terraza'), (6, 'comedor', 'patio'),
    (14, 'sala de estar', 'habitación 1'), (4, 'sala de estar', 'baño 1'),
    (5, 'cochera', 'quincho'), (4, 'cochera', 'patio'),
    (7, 'quincho', 'terraza'), (4, 'habitación 1', 'habitación 2'),
    (3, 'habitación 1', 'baño 2'), (2, 'habitación 2', 'baño 2'),
    (8, 'habitación 2', 'terraza'), (5, 'baño 1', 'baño 2'),
]


def cargar_casa() -> Graph:
    g = Graph(is_dir=False)                         # grafo no dirigido .a
    for ambiente in AMBIENTES:                      # vertices .a
        g.add_vertex(ambiente)
    for metros, origen, destino in PASILLOS:        # aristas .b
        g.add_edge(metros, origen, destino)
    return g


def grados(g: Graph):
    "devuelve la cantidad de aristas (conexiones directas) por ambiente"
    return {v.value: len(v.edges) for v in g}


def punto_c(g: Graph):
    "obtiene el Árbol de Expansión Mínimo con Kruskal y calcula metros totales"
    min_tree = g.kruskal('cocina')
    total = 0
    for edge in min_tree.split(';'):
        if edge:
            origen, destino, metros = edge.split('-')
            m_int = int(metros)
            print(f'{origen} - {destino}: {m_int} m')
            total += m_int
    print(f'\nCable necesario para conectar todos los ambientes: {total} m')


def punto_d(g: Graph):
    "obtiene el camino más corto habitación 1 -> sala de estar con dijkstra"
    paths = g.dijkstra('habitación 1')
    destino = 'sala de estar'
    metro_total = None
    camino = []

    # desapila la stack para rastrear el camino desde el destino al origen
    while paths.size() > 0:
        value = paths.pop()  # estructura: [nodo, costo_acumulado, nodo_anterior]
        if value[0] == destino:
            if metro_total is None:
                metro_total = value[1]
            camino.append(value[0])
            destino = value[2]

    camino.reverse()
    print(' -> '.join(camino))
    print(f'cable de red necesario (router -> Smart TV): {metro_total} m')


if __name__ == '__main__':
    casa = cargar_casa()

    print(' b Cantidad de aristas por ambiente')
    for ambiente, grado in grados(casa).items():
        print(f'{ambiente}: {grado} pasillos')

    print('\n c.arbol de expansion minimo')
    punto_c(casa)

    print('\ncamino más corto habitación 1 -> sala de estar')
    punto_d(casa)