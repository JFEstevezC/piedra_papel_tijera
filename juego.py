import random

print("---------------------------------------------")
print("-------JUEGO DE PIEDRA PAPEL Y TIJERA--------")
print("---------------------------------------------")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")

a = int(input("Seleccione la opción: "))

maquina = random.randint(1,3)

if  maquina == 1 and  a == 1:
    r=("Maquina: Piedra \nJugador: Piedra")
    r1=("Se declara empate")
elif maquina == 2 and  a == 2:
    r= ("Maquina: Papel \nJugador: Papel")
    r1 =("Se declara empate")
elif maquina == 3 and  a == 3:
    r =("Maquina: Tijeras \nJugador: Tijeras")
    r1 =("Se declara empate")
elif maquina == 1 and  a == 2:
    r =("Maquina: Piedra \nJugador: Papel")
    r1 =("El jugador gana la partida")
elif maquina == 1 and  a == 3:
    r =("Maquina: Piedra \nJugador: Tijeras")
    r1 =("El jugador pierde la partida")
elif maquina == 2 and  a == 1:
    r =("Maquina: Papel \nJugador: Piedra")
    r1 =("El jugador pierde la partida")
elif maquina == 2 and  a == 3:
    r =("Maquina: Papel \nJugador: Tijeras")
    r1 =("El jugador gana la partida")
elif maquina == 3 and  a == 1:
    r =("Maquina: Tijeras \nJugador: Piedra")
    r1 =("El jugador gana la partida")
elif maquina == 3 and  a == 2:
    r =("Maquina: Tijeras \nJugador: Papel")
    r1 =("El jugador pierde la partida")

print("----------------------------------------------")
print("-------------RESULTADOS DEL JUEGO-------------")
print("----------------------------------------------")
print(r)
print(r1)

