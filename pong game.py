import pyglet 
from pyglet.shapes import Rectangle
from pyglet.shapes import Circle 
from pyglet.window import key
from pyglet.gl import *
window = pyglet.window.Window(1000,600, "Pong Game")
ball = Circle(x=50,y=300,radius=10,color=(0,0,0))
ball.dx= 200
ball.dy= 200
paddle1 = Rectangle(x=20,y=250,width=10,height=100,color=(0,0,255))
paddle2 = Rectangle(x=950,y=250,width=10,height=100,color=(255,255,255))
wall = Rectangle(x=490,y=0,width=15,height=600,color=(0,0,0,128))
score = int(0)
score_label = pyglet.text.Label(text=f'Score:{score}',font_size=20, x=10, y=575)
keys = pyglet.window.key.KeyStateHandler()
window.push_handlers(keys)
def on_key_press(symbol, modifiers):
    if symbol == key.ESCAPE:
        window.close()
def reset_ball():
     global score
     ball.x = 50
     ball.y = 300
     score = 0
def on_update(dt):
     global score
     ball.x += ball.dx * dt
     ball.y += ball.dy * dt
     if ball.y <= 0 or ball.y >= 600- 10:
            ball.dy = -ball.dy
     if (ball.x <= paddle1.x + 10 and paddle1.y <= ball.y <= paddle1.y + 100):
          ball.dx = -ball.dx
     elif(ball.x + 10 >= paddle2.x and paddle2.y <= ball.y <= paddle2.y + 100):
            ball.dx = -ball.dx
            score += 1
     if(ball.x >= 1000 or ball.x < 0):
         reset_ball() 
def update(dt):
    if keys[key.W] and paddle2.y < 600 - 100:
        paddle2.y += 300 * dt
    if keys[key.S] and paddle2.y > 0:
        paddle2.y -= 300 * dt
    if paddle1.y + 100 / 2 < ball.y and paddle1.y < 600 - 100:
        paddle1.y += 200 * dt
    if paddle1.y + 100 / 2 > ball.y and paddle1.y > 0:
        paddle1.y -= 200 * dt
    

@window.event
def on_draw():
    glClearColor(0.25, 0.875, 0.816, 1) 
    glClear(GL_COLOR_BUFFER_BIT) 
    paddle1.draw()
    paddle2.draw()
    ball.draw()
    wall.draw()
    score_label.draw()
    score_label.text = f'Score: {score}'
pyglet.clock.schedule_interval(update,1/60)
pyglet.clock.schedule_interval(on_update,1/120)
pyglet.app.run()
