from DataStructures.List import single_linked_list as lt
import math

def mayor_diferencia(lst):
    """
    Calcular la mayor diferencia (positiva) entre dos elementos de una lista enlazada de números.

    :param lst: lista enlazada de números, con mínimo 2 elementos.
    :type lst: dict (representando una lista enlazada)
    
    return número positivo como la mayor diferencia entre dos elementos.
    """
    if lt.size(lst) == 0:
        return None
    
    if lt.size(lst) == 1:
        return 0
    
    if lt.size(lst) == 2:
        return math.fabs(lst["first"]["info"] - lst["last"]["info"])
    
    else:
        actual = lst["first"]
        max = lst["first"]["info"]

        while actual != None:
            if actual["next"]["info"] > max:
                max = actual["next"]["info"]
            actual = actual["next"]
        
        actual = lst["first"]
        min = lst["first"]["info"]

        while actual != None:
            if actual["next"]["info"] < min:
                min = actual["next"]["info"]
            actual = actual["next"]
        
        return math.fabs(max - min)

