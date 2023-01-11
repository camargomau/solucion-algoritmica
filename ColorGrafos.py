def clear_screen():                     # Función no muy relevante para el programa, solo sirve para limpiar la pantalla

    import os

    if os.name == 'posix':               # Revisar si el sistema operativo es Mac o Linux
        _ = os.system('clear')
    else:
        _ = os.system('cls')

clear_screen()

def start_from_node(G, node_count):     # Función para ordenar el diccionario de nodos según el nodo inicial

    node_list = list(G.keys())          # Crear lista con las llaves
    adjacent_list = list(G.values())    # Crear lista con los valores de cada llave

    while node_list.index(start_node) != 0:         # Repetir el ordenamiento hasta que el nodo elegido sea el primer elemento de la lista

        buffer = node_list[0]
        buffer_a = adjacent_list[0]

        for i in range(1, node_count):              # Recorrer nodos y valores un lugar a la izquierda, pasando el último al final
            node_list[i-1] = node_list[i]
            adjacent_list[i-1] = adjacent_list[i]

        node_list[node_count-1] = buffer
        adjacent_list[node_count-1] = buffer_a

    sorted_graph = dict(zip(node_list, adjacent_list))  # Unir llaves y valores en un nuevo diccionario

    return sorted_graph

def get_order(G):                       # Función para determinar el orden en el que se analizarán los nodos (i.e. ningún nodo adyacente puede ir seguido en la lista de orden)

    node_list = list(G.keys())

    order_list = list()             # Crear la lista de orden

    while True:     # Ciclo while True para repetir hasta que se llegue a un return

        scanned_node = node_list[0]         # Iniciar por escanear en el primer nodo
        rejected = list() 

        for node in node_list:

            if node in G[scanned_node]:     # Determinar si el nodo es vecino del nodo escaneado. Si es así, agregar a una lista de rechazados
                rejected.append(node)
            else:
                order_list.append(node)     # Si no es vecino, agregarlo a la lista de orden
                scanned_node = node         # Y convertirlo en el elemento escaneado
        else:
            if len(rejected) == 0:                  # Si al final del ciclo for, rejected está vacío, terminar la función 
                return order_list
            else:                                   # Si no, analizar de nuevo esta vez tomando como base a los rechazados
                node_list = rejected

def first_available(colour_list):       # Función para regresar el entero no-negativo más pequeño que no esté en lista de colores

    colour_set = set(colour_list)
    count = 0
    while True:
        if count not in colour_set:  # Determinar si el número ya se encuentra en la lista de colores
            return count            # Regresar con el número y terminar la función
        count += 1
        
def greedy_colour(G, order):            # Función para determinar la coloración

    colour = dict()
    
    for node in order:

        # Agregar el color de un vecino a la lista de usados si el vecino ya tiene asignado un color

        used_neighbour_colours = list() 
        for nbr in G[node]:                                     # Iterar por cada vecino del nodo
            if nbr in colour:                                   # Determinar si el vecino ya tiene asignado un color
                used_neighbour_colours.append(colour[nbr])      # Agregar el color del vecino a la lista de usados

        # Asignarle el primer color disponible al nodo

        colour[node] = first_available(used_neighbour_colours)

    return colour

# Introducción de tamaño de grafo

while True:

    node_num = input("Introduzca la cantidad de nodos que tiene el grafo:\n> ")

    try:
        node_num = int(node_num)                    # Convertir la entrada a un entero; solicitar otra entrada si es necesario
        break
    except:
        clear_screen()
        print("Introduzca un número.")

graph = dict()

clear_screen()

# Introducción de nodos y adyacentes (creación del grafo)

for i in range(node_num):

    print("Introduzca el nombre del nodo ", i+1, ":", sep = '')
    node_name = input("> ")
    
    print("\nInserte los nodos adyacentes a este nodo, separándolos por comas:")
    adj_list = input("> ")
    adj_list_sep = adj_list.split(",")

    graph[node_name] = adj_list_sep         # Se le asigna a cada nodo su lista de adyacentes"

    clear_screen()

# Impresión del grafo

print("El grafo introducido consiste en los siguientes nodos:")

for node, adj_values in graph.items():

    print("\n• El nodo ", node, ", adyacente a los nodos ", sep = '', end = "")

    for adj in list(graph[node]):                       # Imprimir los nodos, especificando una sintaxis distinta si se trata del primero
        if adj == list(graph[node])[0]:
            print(adj, sep = '', end = "")
        else:
            print(", ", adj, sep = '', end = "")
    else:
        print(".")

input("\n(presione enter para continuar)")
clear_screen()

# Introducción de nodo inicial

while True:

    start_node = input("Introduzca el nombre del nodo desde el cual desea iniciar a colorear:\n> ")

    if start_node in list(graph.keys()):
        break
    else:
        clear_screen()
        print("Introduzca un nodo que esté en el grafo.")

# Procesamiento de datos

reordered_graph = start_from_node(graph, node_num)              # Reordenamiento del grafo según el nodo inicial deseado
node_order = get_order(reordered_graph)                         # Obtener el orden en el que se irán coloreando los nodos       
coloured_graph = greedy_colour(reordered_graph, node_order)     # Colorear el grafo

graph_by_colours = dict()                                               # Crear un diccionario "invertido", en el que ahora las llaves sean los colores y los valores los nodos con dicho color
for node_name, colour in coloured_graph.items():
    graph_by_colours.setdefault(colour, list()).append(node_name)

# Introducción de nombres de colores

colour_count = len(list(graph_by_colours.keys()))               # Obtener número de colores
clear_screen()

print("La coloración del grafo resultó en", colour_count, "colores.")

for colour_i in range(colour_count):                                    # Cambiar el números de colores por nombres
    print("\nIntroduzca el nombre del color ", colour_i+1, ":", sep = '')
    colour_name = input("> ")
    graph_by_colours[colour_name] = graph_by_colours.pop(colour_i)

clear_screen()

# Impresión de resultados

for clr in list(graph_by_colours.keys()):               # Imprimir los nodos para cada color

    print("Coloree de color", clr, "los nodos:\n")

    for node in list(graph_by_colours[clr]):
        print("•", node)
    else:
        print("\n", end = "")

input("(presione enter para salir del programa)")
clear_screen()