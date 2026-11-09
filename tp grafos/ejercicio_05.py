from graph import Graph

def cargar_red() -> Graph:
    g = Graph(is_dir=False)

    equipos = [
        ('Manjaro', 'pc'), ('Parrot', 'pc'), ('Fedora', 'pc'),
        ('Ubuntu', 'pc'), ('Mint', 'pc'),
        ('Red Hat', 'notebook'), ('Debian', 'notebook'), ('Arch', 'notebook'),
        ('Guaraní', 'servidor'), ('MongoDB', 'servidor'),
        ('Router 1', 'router'), ('Router 2', 'router'), ('Router 3', 'router'),
        ('Switch 1', 'switch'), ('Switch 2', 'switch'),
        ('Impresora', 'impresora'),
    ]
    for nombre, tipo in equipos:
        g.add_vertex(nombre, tipo)

    conexiones = [
        (40, 'Manjaro', 'Switch 2'), (12, 'Parrot', 'Switch 2'),
        (5, 'MongoDB', 'Switch 2'), (56, 'Arch', 'Switch 2'),
        (3, 'Fedora', 'Switch 2'), (61, 'Switch 2', 'Router 3'),
        (50, 'Router 3', 'Router 2'), (43, 'Router 3', 'Router 1'),
        (37, 'Router 2', 'Router 1'), (9, 'Guaraní', 'Router 2'),
        (25, 'Red Hat', 'Router 2'), (29, 'Router 1', 'Switch 1'),
        (17, 'Debian', 'Switch 1'), (18, 'Ubuntu', 'Switch 1'),
        (80, 'Mint', 'Switch 1'), (22, 'Impresora', 'Switch 1'),
    ]
    for peso, origen, destino in conexiones:
        g.add_edge(peso, origen, destino)
    return g


def tipo_de(g: Graph, nombre):
    return g[g.search(nombre, 'value')].other_values


def punto_b(g: Graph):
    for inicio in ('Red Hat', 'Debian', 'Arch'):
        print(f'\n--- Barrido en profundidad desde {inicio} ---')
        g.deep_show(inicio)
        print(f'\n--- Barrido en amplitud desde {inicio} ---')
        g.amplitude_show(inicio)


def punto_c(g: Graph):
    for origen in ('Manjaro', 'Red Hat', 'Fedora'):
        paths = g.dijkstra(origen)
        destino = 'Impresora'
        peso_total = None
        camino = []

        while paths.size() > 0:
            value = paths.pop()
            if value[0] == destino:
                if peso_total is None:
                    peso_total = value[1]
                camino.append(value[0])
                destino = value[2]

        camino.reverse()
        print(f'{origen} -> Impresora: {" -> ".join(camino)} (costo {peso_total})')


def punto_d(g: Graph):
    min_tree = g.kruskal('Router 1')
    total = 0
    for edge in min_tree.split(';'):
        if edge:
            origen, destino, peso = edge.split('-')
            peso_int = int(peso)
            print(f'{origen} - {destino} (costo {peso_int})')
            total += peso_int
    print(f'Peso total del árbol de expansión mínimo: {total}')


def mejor_equipo_hacia(g: Graph, destino: str, candidatos: list):
    mejor_equipo = None
    menor_costo = float('inf')
    mejor_camino = []

    for candidato in candidatos:
        paths = g.dijkstra(candidato)
        curr = destino
        costo = None
        camino = []

        while paths.size() > 0:
            val = paths.pop()
            if val[0] == curr:
                if costo is None:
                    costo = val[1]
                camino.append(val[0])
                curr = val[2]
        camino.reverse()

        if costo is not None and costo < menor_costo:
            menor_costo = costo
            mejor_equipo = candidato
            mejor_camino = camino

    return mejor_equipo, menor_costo, mejor_camino


def punto_e(g: Graph):
    pcs = [v.value for v in g if v.other_values == 'pc']
    pc, costo, camino = mejor_equipo_hacia(g, 'Guaraní', pcs)
    print(f'La PC con el camino más corto a Guaraní es {pc}: '
          f'{" -> ".join(camino)} (costo {costo})')


def punto_f(g: Graph):
    pos = g.search('Switch 1', 'value')
    vecinos = [e.destination for e in g[pos].edges]
    computadoras = [v for v in vecinos if tipo_de(g, v) in ('pc', 'notebook')]
    equipo, costo, camino = mejor_equipo_hacia(g, 'MongoDB', computadoras)
    print(f'Del switch 1, la computadora más cercana a MongoDB es {equipo}: '
          f'{" -> ".join(camino)} (costo {costo})')


def punto_g(g: Graph):
    g.delete_edge('Switch 1', 'Impresora')
    g.add_edge(22, 'Router 2', 'Impresora')
    punto_b(g)


if __name__ == '__main__':
    red = cargar_red()
    print(' b. Barridos ==='); punto_b(red)
    print('\n=== c. Camino más corto a la impresora ==='); punto_c(red)
    print('\n=== d. Árbol de expansión mínimo ==='); punto_d(red)
    print('\n=== e. PC (no notebook) más cercana a Guaraní ==='); punto_e(red)
    print('\n=== f. Computadora del switch 1 más cercana a MongoDB ==='); punto_f(red)
    print('\n=== g. Impresora conectada al Router 2 ==='); punto_g(red)
