import random

victorias_x = 0
victorias_o = 0

def crear_tablero():
    tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    return tablero

def imprimir_tablero(tablero):
    print(f" 0 1 2")
    print(f"0{tablero[0][0]}|{tablero[0][1]}|{tablero[0][2]}")
    print(" -----")
    print(f"1{tablero[1][0]}|{tablero[1][1]}|{tablero[1][2]}")
    print(" -----")
    print(f"2{tablero[2][0]}|{tablero[2][1]}|{tablero[2][2]}")

def movimiento_jugador(tablero, jugador):
    while True:
        fila = int(input("Elige fila (0, 1, 2): "))
        columna = int(input("Elige columna (0, 1, 2): "))
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            break
        else:
            print("¡Casilla ocupada!")

def hay_ganador(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True
    return False

def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True

def movimiento_ia(tablero, jugador):
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ": #si encuentra la casilla vacia 
                tablero[i][j] = "X"  # simula el poner una x
                if hay_ganador(tablero): #si la IA detecta que podria ganar 
                    tablero[i][j] = "O"  #la tapa con una o
                    return # termina el turno
                tablero[i][j] = " " #deshace la jugada
    
    casillas_vacias = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == " "]
    if casillas_vacias:
        fila, columna = random.choice(casillas_vacias)
        tablero[fila][columna] = jugador

def juego_completo():
    global victorias_x, victorias_o
    tablero = crear_tablero()
    jugador_actual = "X"
    
    while True:
        imprimir_tablero(tablero)
        print(f"Turno de {jugador_actual}")
        
        if jugador_actual == "X":
            movimiento_jugador(tablero, jugador_actual)
        else:
            movimiento_ia(tablero, jugador_actual)

        if hay_ganador(tablero):
            imprimir_tablero(tablero)
            print(f"¡{jugador_actual} ha ganado!")
            if jugador_actual == "X":
                victorias_x = victorias_x + 1
            else:
                victorias_o = victorias_o + 1
            break
            
        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("¡Empate!")
            break
            
        if jugador_actual == "O":
            jugador_actual = "X"
        else:
            jugador_actual = "O"
    
    print("Victorias hasta ahora:")
    print(f"Jugador X: {victorias_x}")
    print(f"Maquina O: {victorias_o}")

while True:
    juego_completo()
    repetir = input("¿Quieres jugar otra vez? (s/n): ")
    if repetir.lower() != "s":
        break