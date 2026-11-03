from typing import Any, Optional

from queue_ import Queue
class Node():

    def __init__(self, value=None, other_values=None):
        self.value = value
        self.left = None
        self.right = None
        self.other_values = other_values
        self.height = 0
    
    def __str__(self):
        return self.value


class BinaryTree():

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height
    
    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

    def insert_node(self, value: Any, other_value=None) -> None:

        def __insert_node(root, value, other_value=None):
            if root is None:
                # print(f'lugar vacio insertar {value}')
                root = Node(value, other_value)
            elif value < root.value:
                # print(f'ir a la izquierda de {root.value}')
                root.left = __insert_node(root.left, value, other_value)
            else:
                # print(f'ir a la derecha de {root.value}')
                root.right = __insert_node(root.right, value, other_value)
            
            root = self.auto_balance(root)
            self.update_height(root)
            return root
            
        self.root = __insert_node(self.root, value, other_value)

    def delete_node(self, value: Any) -> Optional[Any]:

        def __replace(root):
            if root.right is None:
                return root.left, root
            root.right, aux = __replace(root.right)
            root = self.auto_balance(root)
            self.update_height(root)
            return root, aux

        def __delete_node(root, value):
            x = None
            other_value = None
            if root is not None:
                if value < root.value:
                    root.left, x, other_value = __delete_node(root.left, value)
                elif value > root.value:
                    root.right, x, other_value = __delete_node(root.right, value)
                else:
                    x = root.value
                    other_value = root.other_values
                    if root.left is None:
                        return root.right, x, other_value
                    elif root.right is None:
                        return root.left, x, other_value
                    else:
                        root.left, aux = __replace(root.left)
                        root.value = aux.value
                        root.other_values = aux.other_values
                root = self.auto_balance(root)
                self.update_height(root)
            return root, x, other_value

        self.root, x, other_value = __delete_node(self.root, value)
        return x, other_value

    def search(self, value) -> Optional[Any]:
        def __search(root, value):
            aux = None
            if root is not None:
            
                if root.value == value:
                    aux = root
                elif value < root.value:
                    aux = __search(root.left, value)
                elif value > root.value:
                    aux = __search(root.right, value)

            return aux


        node = __search(self.root, value)
        
        return node 
    
    def auto_balance(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def simple_rotation(self, root, control):
        if control: # rotaicon hacia la derecha
            aux = root.left
            root.left = aux.right
            aux.right = root
        else: # rotacion hacia la izquierda
            aux = root.right
            root.right = aux.left
            aux.left = root
        
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root
    
    def double_rotation(self, root, control):
        if control: # rotacion doble a la derecha
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else: # rotacion doble izquierda
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def inorden(self) -> None:
        
        def __inorden(root):
            if root.left is not None:
                # print(f'anda a la izquierda de {root.value}')
                __inorden(root.left)
            # print(f'procesa nodo actual')
            print(root.value, root.height)
            if root.right is not None:
                # print(f'anda a a derecha de {root.value}')
                __inorden(root.right)

        __inorden(self.root)
    
    def postorden(self) -> None:
        
        def __postorden(root):
            if root.right is not None:
                __postorden(root.right)
            print(root.value)
            if root.left is not None:
                __postorden(root.left)

        __postorden(self.root)

    def preorden(self) -> None:
        def __preorden(root):
            print(root.value)
            if root.left is not None:
                __preorden(root.left)
            if root.right is not None:
                __preorden(root.right)

        __preorden(self.root)

    def by_level(self) -> None:

        pendings = Queue()

        if self.root is not None:
            pendings.arrive(self.root)
            # print(f'queue')
            # pendings.show()
            # input()
            while pendings.size() > 0:
                node = pendings.attention()
                print(node.value)
                # input()
                if node.left is not None:
                    pendings.arrive(node.left)
                if node.right is not None:
                    pendings.arrive(node.right)
                # print(f'queue ')
                # pendings.show()
                # input()

    def inorden_villain(self) -> None:

        def __inorden_villain(root):
            if root.left is not None: 
                __inorden_villain(root.left)
            if not root.other_values['is_hero']:
                print(root.value)
            if root.right is not None:
                __inorden_villain(root.right)

        if self.root is not None:
            __inorden_villain(self.root)

    def postorden_hero(self):
    
        def __postorden_hero(root):
            if root.right is not None:
                __postorden_hero(root.right)
            if root.other_values['is_hero']:
                print(root.value)
            if root.left is not None:
                __postorden_hero(root.left)

        __postorden_hero(self.root)

    def inorden_hero_star_with(self, prefix: str) -> None:

        def __inorden_hero_star_with(root, prefix):
            if root.left is not None:
                __inorden_hero_star_with(root.left, prefix)
            if root.value.startswith(prefix) and root.other_values['is_hero']:
                print(root.value)
            if root.right is not None:
                __inorden_hero_star_with(root.right, prefix)

        if self.root is not None:
            __inorden_hero_star_with(self.root, prefix)

    def proxy_search(self, prefix: str) -> list:

        def __proxy_search(root, prefix, found): #funcion interna recursiva
            if root.left is not None: #baja la rama izquierda si no esta vacía y la revisa entera antes d seguir con el nodo actual
                __proxy_search(root.left, prefix, found)  #mira nodo izquierdo, prefijo "stra" y lista found
            if prefix in root.value.lower(): #pasa el nombre a minusculas y pregunta si el prefijo esta dentro del nombre
                found.append(root) #si coincide guarda el nodo entero en la lista
            if root.right is not None: #baja por la derecha
                __proxy_search(root.right, prefix, found)

        found = [] #crea la lista vacia
        if self.root is not None: #si el arbol no esta vacio
            __proxy_search(self.root, prefix, found) #arranca el recorrido desde la raiz
        return found #devuelve la lista con los nodos q coincidieron

    def count_heroes(self) -> None:
        def __count_heroes(root):
            count = 0
            if root is not None:
                if root.left is not None:
                    count += __count_heroes(root.left)
                if root.other_values['is_hero']:
                    count += 1
                if root.right is not None:
                    count += __count_heroes(root.right)
            return count

        count = __count_heroes(self.root)
        return count

    def count_nodes(self) -> int:

        def __count_nodes(root):
            if root is None:
                return 0
            return 1 + __count_nodes(root.left) + __count_nodes(root.right)

        return __count_nodes(self.root)


    # a. listado inorden de criaturas y quien las derroto
    def inorden_criaturas(self) -> None:

        def __inorden_criaturas(root):
            if root.left is not None:
                __inorden_criaturas(root.left)
            vencedor = root.other_values['derrotado_por']
            if vencedor is None:
                print(root.value, '- Sin derrotar')
            else:
                print(root.value, '-', vencedor)
            if root.right is not None:
                __inorden_criaturas(root.right)

        if self.root is not None:
            __inorden_criaturas(self.root)

    # e. criaturas derrotadas por un heroe o dios
    def inorden_derrotadas_por(self, heroe: str) -> None:

        def __inorden_derrotadas_por(root, heroe):
            if root.left is not None:
                __inorden_derrotadas_por(root.left, heroe)
            if root.other_values['derrotado_por'] == heroe:
                print(root.value)
            if root.right is not None:
                __inorden_derrotadas_por(root.right, heroe)

        if self.root is not None:
            __inorden_derrotadas_por(self.root, heroe)

    # f. criaturas que no fueron derrotadas
    def inorden_sin_derrotar(self) -> None:

        def __inorden_sin_derrotar(root):
            if root.left is not None:
                __inorden_sin_derrotar(root.left)
            if root.other_values['derrotado_por'] is None:
                print(root.value)
            if root.right is not None:
                __inorden_sin_derrotar(root.right)

        if self.root is not None:
            __inorden_sin_derrotar(self.root)

    # n. criaturas capturadas por un heroe o dios
    def inorden_capturadas_por(self, heroe: str) -> None:

        def __inorden_capturadas_por(root, heroe):
            if root.left is not None:
                __inorden_capturadas_por(root.left, heroe)
            if root.other_values['capturada'] == heroe:
                print(root.value)
            if root.right is not None:
                __inorden_capturadas_por(root.right, heroe)

        if self.root is not None:
            __inorden_capturadas_por(self.root, heroe)

    # d paso 1) carga en el arbol "destino" cuantas criaturas derroto cada vencedor
    def contar_victorias(self, destino) -> None:

        def __contar_victorias(root):
            if root.left is not None:
                __contar_victorias(root.left)
            vencedor = root.other_values['derrotado_por']
            if vencedor is not None:
                nodo = destino.search(vencedor)
                if nodo is None:
                    destino.insert_node(vencedor, {'cantidad': 1})
                else:
                    nodo.other_values['cantidad'] += 1
            if root.right is not None:
                __contar_victorias(root.right)

        if self.root is not None:
            __contar_victorias(self.root)

    # dpaso 2. arma un arbol ordenado por (cantidad, nombre)
    def armar_ranking(self, destino) -> None:

        def __armar_ranking(root):
            if root.left is not None:
                __armar_ranking(root.left)
            destino.insert_node((root.other_values['cantidad'], root.value))
            if root.right is not None:
                __armar_ranking(root.right)

        if self.root is not None:
            __armar_ranking(self.root)

    # dpaso 3. muestra los primeros "cantidad" de mayor a menor
    #inorden invertido: derecha, nodo, izquierda
    def top_ranking(self, cantidad: int) -> None:

        def __top_ranking(root, restantes):
            if root is None or restantes == 0:
                return restantes
            restantes = __top_ranking(root.right, restantes)
            if restantes > 0:
                print(root.value[1], '-', root.value[0])
                restantes -= 1
            restantes = __top_ranking(root.left, restantes)
            return restantes

        __top_ranking(self.root, cantidad)
        
        
    def inorden_pokemon_numero(self):
        def _inorden(nodo):
            if nodo is not None:
                _inorden(nodo.left)
                print(nodo.value, nodo.other_values['nombre'])
                _inorden(nodo.right)

        _inorden(self.root)

    
    def inorden_pokemon_nombre(self):
        def _inorden(nodo):
            if nodo is not None:
                _inorden(nodo.left)
                print(nodo.other_values['nombre'])
                _inorden(nodo.right)

        _inorden(self.root)


    def inorden_cantidad_por_tipo(self):
        def _inorden(nodo):
            if nodo is not None:
                _inorden(nodo.left)
                print(nodo.value, len(nodo.other_values))
                _inorden(nodo.right)

        _inorden(self.root)

    def inorden_debiles_frente_a(self, tipos_atacante):
        tipos_atacante = [tipo.lower() for tipo in tipos_atacante]

        def _inorden(nodo):
            if nodo is not None:
                _inorden(nodo.left)

                debilidades = [
                    tipo.lower()
                    for tipo in nodo.other_values['debilidades']
                ]

                if any(tipo in debilidades for tipo in tipos_atacante):
                    print(nodo.other_values['nombre'])

                _inorden(nodo.right)

        _inorden(self.root)

    def contar_con_mega(self):
        def _contar(nodo):
            if nodo is None:
                return 0

            actual = 1 if nodo.other_values['mega'] else 0
            return actual + _contar(nodo.left) + _contar(nodo.right)

        return _contar(self.root)

    def contar_con_gigamax(self):
        def _contar(nodo):
            if nodo is None:
                return 0

            actual = 1 if nodo.other_values['gigamax'] else 0
            return actual + _contar(nodo.left) + _contar(nodo.right)

        return _contar(self.root)