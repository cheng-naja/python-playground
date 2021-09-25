c = ['red', 'blue']
dist = 500

from turtle import *
hideturtle()
speed(11)

while True:
  color(c[dist%2])
  forward(dist)
  left(90)
  dist = dist - 3