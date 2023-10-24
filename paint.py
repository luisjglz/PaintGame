"""
Juego: Paint
Programador 1: Luis José González
Programador 2: Humberto Alejandro Rosas Téllez (HART) 
Programador 3: Arturo el Rey
Programador 4: elhector
Programador 5: Octavio Augusto Aleman Esparza
Programador 6: Alejandro Díaz Villagómez
Programador 7: Arturo el Rey
Programador 8: Armando Mandujano 
Programador 9: Octavio Augusto Aleman Esparza
Programador 10: Alejandro Díaz Villagómez
Programador 11: Arturo el Rey
Programador 12: Rodrigo Aldahir Rosete 
Programador 13: Diego Isunza Garciacano
Programador 14: Daniel Alejandro Martinez Rosete
Programador 15: Diego Jacobo Martínez
Programador 16: Iván Santiago Hernández Mendoza
Programador 17: CARLAO

Fecha: 9 / mayo / 2022    

Otro comment jiji
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    pass  # TODO


def rectangle(start, end):
    """Draw rectangle from start to end."""
    pass  # TODO


def triangle(start, end):
    """Draw triangle from start to end."""
    pass  # TODO


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()


#Amigos mios Estamos probando. 