from decimal import Decimal             # Importar el tipo de dato decimal para utilizarlo en lugar del float (que es muy inexacto para el dinero)

# Función no muy relevante para el programa, solo sirve para limpiar la pantalla

def clear_screen():

    import os

    if os.name == 'posix':               # Revisar si el sistema operativo es Mac o Linux
        _ = os.system('clear')
    else:
        _ = os.system('cls')

clear_screen()

# Función que determina el número de monedas de cierta denominación a usar

def coin_count(coin_list,amount):
                                 
    coin_list = sorted(coin_list, reverse = True)       # Las denominaciones a usar vienen como una lista que luego se ordena de mayor a menor
    coin_set = dict()                                  # El conjunto de monedas óptimo se representará por un diccionario con las denominaciones como llaves 

    for denom in coin_list:                         # Determinar el número de monedas para cada denominación en la lista
        coin_set[denom] = int(amount/denom)            # El número de monedas es simplemente la parte entera de la división amount/denom
        amount = amount % denom                         # Definimos la cantidad de dinero como el residuo de la división

    return coin_set

# Introducción del cambio que se desea dar

change = Decimal(input("Introduzca el cambio que desea dar:\n> "))

# Introducción de denominaciones de monedas disponibles

print("\nIntroduzca las denominaciones de monedas disponibles, separándolas por comas:")     
coins = input("> ")
coins = coins.split(",")            # Se crea una lista con todas las denominaciones insertadas

for i in range(len(coins)):         # Se convierte cada elemento en la lista a un Decimal
    coins[i] = Decimal(coins[i])

# Procesamiento de datos

optimal_coins = coin_count(coins,change)        # Determinar el conjunto óptimo de monedas

total_coin_count = 0
for denom in optimal_coins:                     # Determinar el conteo total de monedas
    if optimal_coins[denom] != 0:
        total_coin_count = total_coin_count + optimal_coins[denom]

coin_sum = 0                                    # Determinar la suma de dinero de todas las monedas en el conjunto óptimo
for denom in optimal_coins:
    if optimal_coins[denom] != 0:
        coin_sum = coin_sum + (denom * optimal_coins[denom])

# Impresión de resultados

clear_screen()
print("Para dar $", change, ", la menor cantidad de monedas a utilizar es de:\n", sep = "")

for denom in optimal_coins:                                                         # Imprimir la cantidad de monedas para cada denominación
    if optimal_coins[denom] == 1:                                                       # Imprimir en singular para 1 moneda
        print("• ", optimal_coins[denom], " moneda de $", denom, sep = "") 
    elif optimal_coins[denom] > 1:                                                      # Imprimir en plural para más de 1 moneda
        print("• ", optimal_coins[denom], " monedas de $", denom, sep = "")

if total_coin_count == 1:                                                           # Imprimir el total de monedas
    print("\nTotal: ", total_coin_count, " moneda, ", sep = "", end = "")  
elif total_coin_count > 1:                                                              # Imprimir en singular o plural según sea le caso
    print("\nTotal: ", total_coin_count, " monedas, ", sep = "", end = "")

print("$", coin_sum, ".", sep = "")                                                 # Imprimir la suma total del conjunto óptimo de monedas

if change != coin_sum:                                                              # Imprimir si faltó cierta cantidad de dinero por falta de denominaciones
    if change-coin_sum == 1:                                                                                                             # Imprimir en singular para $1
        print("\nFaltaría $", change-coin_sum, ", ya que no hay una denominación de monedas lo suficientemente pequeña.", sep = "")
    else:                                                                                                                                # Imprimir en plural para más de $1
        print("\nFaltarían $", change-coin_sum, ", ya que no hay una denominación de monedas lo suficientemente pequeña.", sep = "")

input("\n(presione enter para salir del programa)")
clear_screen()