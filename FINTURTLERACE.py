from turtle import *
from random import randint

speed(0)
penup()
goto(-140, 140)

for step in range(15):
  write(step, align='center')
  right(90)
  for num in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

for turn in range(10):
  ada.right(36)

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()

for turn in range(72):
  bob.left(5)

olaf = Turtle()
olaf.shape('turtle')
olaf.color('green')

olaf.penup()
olaf.goto(-160, 40)
olaf.pendown()

for turn in range(60):
  olaf.right(6)

berta = Turtle()
berta.shape('turtle')
berta.color('orange')

berta.penup()
berta.goto(-160, 10)
berta.pendown()

for turn in range(30):
  berta.left(12)

for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  olaf.forward(randint(1,5))
  berta.forward(randint(1,5))