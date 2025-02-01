from turtle import *
from random import randint
from time import sleep

def catch(x, y):
  points = points + 1
  t.write("BURDA!")
  new_x = randint(-200, 200)
  new_y = randint(-200, 200)
  t.goto(new_x, new_y)
  
t = Turtle()
t.shape("turtle")  # Kaplumbağa şeklinde olsun
t.color("green")  # Yeşil renk olsun
points = 0  # Başlangıçta puan 0

t.penup()
# dökümantasyon burda https://docs.python.org/3/library/turtle.html#turtle.onclick
t.onclick(catch)  # Kullanıcı kaplumbağaya tıkladığında 'catch' fonksiyonunu çalıştır

while points < 3:
  sleep(1.5) # 1.5 saniye bekle
  new_x = randint(-200, 200) # Rastgele x koordinatı belirle
  new_y = randint(-200, 200)  # Rastgele y koordinatı belirle
  t.goto(new_x, new_y)  # Kaplumbağayı yeni koordinatlara götür
  
t.write("KAZANDIN !")
t.hideturtle()
