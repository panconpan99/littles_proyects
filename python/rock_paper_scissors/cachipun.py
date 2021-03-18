import random
#rock papers scissors
#commonly known as cachipun in chile
lista=['piedra','papel','tijera']
def winner(n, jugador, computador):
    if n == 1:
        print('el jugador gano')
        jugador+=1
    else:
        print('el computador gano')
        computador+=1
    return jugador, computador

computador = c= 0
jugador = j = 0
run = True
while run:
    elegir_computador = random.choice(lista)
    elegir_jugador = input('piedra papel o tijera o salir: ')
    print("jugador lanzo "+elegir_jugador)
    if elegir_jugador == 'salir':
        break
    print("el computador lanzo "+elegir_computador)
    if elegir_computador == elegir_jugador:
        print('empate')
    elif elegir_jugador== 'piedra':
        if elegir_computador == 'tijera':
            j,c = winner(1,j,c)
        else:
            j,c = winner(0,j,c)
    elif elegir_jugador == 'tijera':
        if elegir_computador == 'papel':
            j,c= winner(1,j,c)
        else:
            j,c = winner(0,j,c)
    elif elegir_jugador == 'papel':
        if elegir_computador == 'piedra':
            j,c=winner(1,j,c)
        else:
            j,c=winner(0,j,c)
    else:
        print("comando erroneo")

    print("")
    print("puntaje: jugador = "+ str(j) + " computador = " +str(c))
    print("")

    
