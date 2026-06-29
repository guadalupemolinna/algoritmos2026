from copy import copy, deepcopy
from typing import Any

class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Any:
        return self.__elements.pop()
    
    def show(self) -> None:
        stack_aux = Stack()

        # vaciamos la pila original, mostramos y guardamos en la auxiliar
        while self.size() > 0: 
            value = self.pop()
            print(value)
            stack_aux.push(value)
        
        # devolvemos los elementos a la pila original para no destruirla
        while stack_aux.size() > 0: 
            value = stack_aux.pop()
            self.push(value)
        
    def size(self) -> int:
        return len(self.__elements)
    
    def on_top(self) -> Any:
        if self.size() > 0:
            return self.__elements[-1]
