
import pyglet 
from pyglet.window import key
from pyglet.shapes import Rectangle
# Create a window
window = pyglet.window.Window(1000,600, "The red box")
rectangle = Rectangle(x=50,y=10,width=100,height=100,color=(0,255,0))
rectangle2 = Rectangle(x=150,y=10,width=100,height=100,color=(255,255,255))
speed=200
player_alive = True 
keys = key.KeyStateHandler()
window.push_handlers(keys)
def update(dt):
   global player_alive 
   if player_alive:  
    if keys[key.LEFT]:
      rectangle.x -= speed * dt
    if keys[key.RIGHT]:
      rectangle.x += speed * dt
    if keys[key.UP]:
      rectangle.y += speed * dt
    if keys[key.DOWN]:
      rectangle.y -= speed * dt
    rectangle.x = max(0,min(window.width - rectangle.width, rectangle.x))
    rectangle.y = max(0,min(window.height - rectangle.height, rectangle.y))
    
    
    if keys[key.A]:
      rectangle2.x -= speed * dt
    if keys[key.D]:
      rectangle2.x += speed * dt
    if keys[key.W]:
      rectangle2.y += speed * dt
    if keys[key.S]:
      rectangle2.y -= speed * dt
    rectangle2.x = max(0,min(window.width - rectangle2.width, rectangle2.x))
    rectangle2.y = max(0,min(window.height - rectangle2.height, rectangle2.y))
    if keys[key.LCTRL]:
     player_alive = False 
@window.event
def on_draw():
    window.clear()
    rectangle.draw()
    rectangle2.draw()
pyglet.clock.schedule_interval(update,1/60)
# Run the application
pyglet.app.run()