# Función no muy relevante para el programa, solo sirve para limpiar la pantalla
def clear_screen():

    import os

    # Revisar si el sistema operativo es Mac o Linux
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

clear_screen()

###
# Entrada de datos

# Introducción de la cantidad de objetos
while True:
    # Entrada del usuario
    obj_num = input("Introduzca la cantidad de objetos a considerar:\n> ")

    # Convertir la entrada a un entero; solicitar otra entrada si es necesario
    try:
        obj_num = int(obj_num)
        break
    except:
        clear_screen()
        print("Introduzca un número.")

# Creación los diccionarios que contendrán el peso y el valor de cada objeto
weight = dict()
value = dict()

# Introducción del peso y del valor de los objetos
for i in range(1, obj_num+1):

    clear_screen()

    # Introducción del peso del objeto
    while True:
        # Entrada del usuario
        print("Introduzca el peso del objeto ", i, ":", sep = '')
        weight[i] = input("> ")

        # Convertir la entrada a un flotante; solicitar otra entrada si es necesario
        try:
            weight[i] = float(weight[i])
            break
        except:
            clear_screen()
            print("Introduzca un número.")

    # Introducción del valor del objeto
    while True:
        # Entrada del usuario
        print("Introduzca el valor del objeto ", i, ":", sep = '')
        value[i] = input("> ")

        # Convertir la entrada a un flotante; solicitar otra entrada si es necesario
        try:
            value[i] = float(value[i])
            break
        except:
            clear_screen()
            print("Introduzca un número.")

###
# Cálculo de la utilidad de cada objeto

# Creación del diccionario que contendrá la razón valor/peso (utilidad)
utility_ratio = dict()
# Cálculo de la razón valor/peso para cada objeto introducido por el usuario
for i in range(1, obj_num+1):
    utility_ratio[i] = value[i]/weight[i]

# Creación del diccionario que tiene los elementos en orden descendente
sorted_utility_ratio = dict(sorted(utility_ratio.items(), key = lambda orig_dict: orig_dict[1], reverse = True))

clear_screen()

###
# Procesamiento de datos (colocación de objetos)

# Introducción de la capacidad de la mochila
while True:
    # Entrada del usuario
    sac_capac = input("Introduzca la capacidad de peso de la mochila:\n> ")

    # Convertir la entrada a un flotante; solicitar otra entrada si es necesario
    try:
        sac_capac = float(sac_capac)
        break
    except:
        clear_screen()
        print("Introduzca un número.")

# Inicialización del peso de la mochila con los objetos (en 0)
weight_sac = 0
# Inicialización del valor total de los objetos en la mochila (en 0)
value_sac = 0
# Creación de la lista de los objetos en la mochila
objs_in_sac = list()

# Colocación de los objetos en la mochila según su razón valor/peso hasta que se no se puedan agregar más 
# Intentar agregar todos los objetos que introdujo el usuario
for i in sorted_utility_ratio:
    # Si al agregar el objeto, el peso de la mochila es menor a su capacidad,
    if weight_sac + weight[i] <= sac_capac:
        # entonces agregar el objeto a la mochila (sumar su peso, su valor y agregarlo a la lista)
        weight_sac = weight_sac + weight[i]
        value_sac = value_sac + value[i]
        objs_in_sac.append(i)
    # Si al agregar el objeto se excede la capacidad, salir del ciclo
    else:
        break

clear_screen()

###
# Impresión de resultados

# Indicar si no se pudo meter ningun objeto a la mochila
if len(objs_in_sac) == 0:
    print("Ningún objeto es lo suficientemente ligero como para llevarlo en la mochila.")
# Si sí se pudieron introducir objetos, se imprimen los objetos, su valor total y su peso total
else:
    # Se ordena la lista de los objetos en la mochila
    sorted_objs = sorted(objs_in_sac)

    print("Al introducir los objetos ", end = "")

    # Impresión de los objetos, especificando una sintaxis distinta si se trata del primero o del último
    for object in sorted_objs:
        # Para el primero
        if object == sorted_objs[0]:
                print(object, sep = "", end = "")
        # Para el último
        elif object == sorted_objs[len(sorted_objs)-1]:
                print(" y ", object, sep = "", end = "")
        else:
            print(", ", object, sep = "", end = "")

    # Impresión del valor total y el peso total
    print(" en la mochila se obtiene el valor máximo, llevando un valor total de ", value_sac, " y un peso total de ", weight_sac, ".\n", sep = "")

input("(presione enter para salir del programa)")
clear_screen()