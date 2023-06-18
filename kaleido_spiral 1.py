import turtle as t

from itertools import cycle
colors = cycle(['red','orange','yellow','green','blue','purple'])

def draw_shape(size):
    t.pencolor(next(colors))
    t.circle(size)
    draw_shape(size+5)
    
    
t.bgcolor ('black')
t.speed('fast')
t.pensize (4)
draw_shape(30)


    
    
