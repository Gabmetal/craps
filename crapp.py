import random
#Tirar los dados
def dados():
    dado1, dado2 = random.randint(1,6), random.randint(1,6)
    print("\nDado 1:", dado1, "\nDado 2:", dado2,"\n")
    sum = dado1 + dado2
    return sum
def round(rnd, beth, cash):
    sum = dados()
    if sum == 7 or sum == 11:
        print("\n Pass", sum)
        cash += beth*2
        return sum, cash
    elif sum == 2 or sum == 3 or sum == 11:
        print("\n Crap", sum)
        return sum, cash
    elif rnd == 0:
        point = sum
        print("El punto es: ", point)
        retry(cash, beth)
        rnd += 1
    else:
        print("El tiro es: ", sum)
        retry(cash, beth)
    return sum, cash
def retry(cash, beth):
    print("Dinero disponible: $", cash)
    x = int(input("\nApostar?\n\t1 Si\n\t2 no\nOpcion:"))
    if x == 1:
        apuesta(cash, beth)
    elif x == 2:
        round()
def balance():
    cash = int(input("\nCantidad de dinero disponible: $"))
    return cash
def apuesta(cash, beth1):
    beth = int(input("\nDinero a apostar: $"))
    cash -= beth
    beth1 += beth
    print("\nDinero disponible: $",cash,"\nApuesta: $",beth1)
    return cash, beth
#def punto():
    #Si la suma de los dados es 7 u 11
    #Imprimir ganaste y sumar lo apostado*2 a la billetera
    #Si es 2, 3 o 12
    #imprimir crap y restar lo apostado a la billetera
    #Sino asignar el valor como punto y pasar a la siguiente ronda.

""" Comenzar el juego
    Ingresar cantidad de dinero
    Preguntar si apuesta
    Tirar dados
    Verificar puntos
    Restar o sumar las apuestas a la billetera en caso de craps o pass
    De no ser crap ni pass pasar a la siguiente ronda
    Preguntar si desea apostar
    Tirar dados
    Comparar
    Restar o sumar las apuestas a la billetera en caso de craps o pass y volver a empezar
    Sino pasar a siguiente ronda"""
def game():
    beth = 0
    beth = 0
    cash = balance()
    beth, cash = apuesta(cash, beth)
    rnd = 0
    tiro, cash = round(rnd,beth,cash)
    print("\nDinero disponible", cash)

game()