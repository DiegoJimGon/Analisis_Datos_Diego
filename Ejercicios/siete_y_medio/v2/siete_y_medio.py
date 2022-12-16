import random
import time
import utilidades as utl

cartas_barajeadas = utl.barajear()

def crearJugador(nombre: str, humano: bool):
    jugador = {
        "nombre": nombre,
        "puntos": 0,
        "cartas": [],
        "humano": humano
    }
    return jugador

def pedirCarta() -> tuple:
    return cartas_barajeadas.pop()


def iniciar():
    nombre = input("Ingresa tu nombre: ")
    jugador1 = crearJugador(nombre, True)
    jugador2 = crearJugador("Polaris", False)
    ganador = inicia_el_juego(jugador1, jugador2)
    if(ganador.get("nombre","no hay ganador")!="no hay ganador"):
        print("El ganador es",ganador["nombre"])
    else:
        print(ganador["mensaje"])

def inicia_el_juego(jugador1, jugador2) -> dict:
    jugar(jugador1)
    jugar(jugador2)
    return verificaGanador(jugador1, jugador2)


def jugar(jugador: dict):
    nombre = jugador["nombre"]
    primera_carta = True
    jugar = True
    while (jugar):
        if (not primera_carta):
            imprimeMano(jugador)
            if (jugador["humano"] and regla(jugador) and int(input(f"{nombre}: quieres otra carta si:1 no:0 - "))):
                ronda(jugador)
            elif (not jugador["humano"] and regla(jugador)):
                jugar = rondaCPU(jugador)
            else:
                jugar = False
        else:
            ronda(jugador)
            primera_carta = False

def ronda(jugador: dict):
    print("Turno:", jugador["nombre"])
    carta = pedirCarta()
    jugador["cartas"].append(carta)
    jugador["puntos"] += carta[1]


def rondaCPU(jugador: dict) -> bool:
    pedir = random.random() >= 0.5
    mnj = "si" if pedir else "no"
    print("quieres otra carta?")
    print(f"{mnj}")
    if (pedir):
        time.sleep(2)
        ronda(jugador)
        return True
    return False


def verificaGanador(jugador1: dict, jugador2: dict) -> dict:
    nombre1 = jugador1["nombre"]
    nombre2 = jugador2["nombre"]
    if (regla(jugador1) and regla(jugador2)):
        if (jugador1['puntos'] == jugador2['puntos']):
            return {"mensaje": "Empate"}
        elif (jugador1['puntos'] < jugador2['puntos']):
            return jugador2
        else:
            return jugador1
    elif (not regla(jugador1) and not regla(jugador2)):
        return {"mensaje": "Ninguno gana"}
    else:
        return jugador1 if regla(jugador1) else jugador2


def regla(jugador: dict) -> bool:
    return jugador["puntos"] <= 7.5

def imprimeMano(jugador:dict):
    for carta in jugador["cartas"]:
        print(carta[0],end=" ")
    print()
iniciar()
