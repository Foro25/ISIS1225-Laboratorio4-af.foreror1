from DataStructures.List import list_node as node
def new_list ():
    new_list = {
    'first': None,
    'last': None,
    'size': 0,
    }
    return new_list

def add_first(my_list, element):
    nuevo = node.new_single_node(element)
    if my_list["size"]==0:
        my_list["first"]= nuevo
        my_list["last"]=nuevo
        my_list["size"]+=1
    else:
        inicial = my_list["first"]
        nuevo["next"] = inicial
        my_list["first"] = nuevo
        my_list["size"] += 1
        
    return my_list

def add_last(my_list, element):
    nuevo = node.new_single_node(element)
    if my_list["size"] == 0:
         my_list["first"] = nuevo
         my_list["last"] = nuevo
    else:
        my_list["last"]["next"] = nuevo
        my_list["last"] = nuevo
    my_list["size"] += 1
    
    return my_list
        

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False
    
def size(my_list):
    return my_list["size"]

def first_element(my_list):
    return my_list["first"]["info"]
    
def last_element(my_list):
    if is_empty(my_list):
        return None
    else:
        return my_list["last"]["info"]

def get_element(my_list, pos):
    if (is_empty(my_list)) or (pos < 0) or (pos > size(my_list)):
        return None
    if pos == 0:
        return my_list["first"]["info"]
    else:
        actual = my_list["first"]
        i = 0
        while (actual != None) and (i != pos):
            actual = actual["next"]
            i += 1    
            if i == pos:
                return actual["info"]

def remove_first(my_list):
    if is_empty(my_list):
        return None 
    else:
        first_nodo = my_list["first"]
        nodo = node.new_single_node(first_nodo)
        info_nodo = nodo["info"]
        my_list["first"] = first_nodo ["next"]
        my_list["size"] -= 1
        if size(my_list) == 0:
            my_list["last"] = None
            my_list["first"] = None
        return info_nodo

def remove_last(my_list):
    if is_empty(my_list):
        return None 
    else:
        actual = my_list ["first"]
        while actual["next"] is not None:
            prev = actual
            actual = actual["next"]
        prev["next"] = None
        my_list["last"] = prev
        my_list["size"] -= 1
        if size(my_list) == 0:
            my_list = new_list()
        return my_list

def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list): 
        return None
    else:
        nodo = node.new_single_node(element)
        if is_empty(my_list) or pos == 0:
            nodo["next"] = my_list["first"]
            my_list["first"] = nodo
            if my_list["size"] == 0:
                my_list["last"] = nodo
        else:
            actual = my_list ["first"]
            i = 0
            while (actual != None) and (i != pos):
                prev = actual
                actual = actual["next"]
                i += 1
            nodo["next"] = actual
            prev["next"] = nodo
            if nodo["next"] is None:
                my_list["last"] = nodo
        my_list["size"] += 1
        
        return my_list

def is_present(my_list, element, cmp_function):
    actual = my_list["first"]
    pos = 0
    while actual != None:
        if cmp_function(element, actual["info"]) == 0:
            return pos
        else:
            pos += 1
            actual = actual["next"]
    return -1

def delete_element(my_list, pos):    
    nodo = my_list["first"]
    nodo_anterior = None
    conteo = 0
    
    while conteo < pos:
        nodo_anterior = nodo
        nodo = nodo["next"]
        conteo += 1
    nodo_actual = nodo
    nodo_posterior = nodo_actual["next"]
    if nodo_anterior == None:
        my_list["first"] = nodo_posterior
    else:
        nodo_anterior["next"] = nodo_posterior
    if nodo_posterior == None:
        my_list["last"] = nodo_anterior
    
    my_list["size"] -= 1
    
    return my_list

def exchange(my_list, pos1, pos2):
    pass

def change_info(my_list, pos, new_info):
    pass

def sub_list(my_list, pos, numelem):
    sub_list = new_list()
    nodo = my_list["first"]
    conteo = 0

    while conteo < pos and nodo != None:
        nodo = nodo["next"]
        conteo += 1

    for nodos in range(numelem):
        if nodo is None:
            break
        nuevo_nodo = node.new_single_node(nodo["info"])
        if sub_list["first"] is None:
            sub_list["first"] = nuevo_nodo
        else:
            sub_list["last"]["next"] = nuevo_nodo
        sub_list["last"] = nuevo_nodo
        sub_list["size"] += 1
        nodo = nodo["next"]

    return sub_list