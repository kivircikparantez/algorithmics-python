from turtle import *
from random import randint
from time import sleep

# Kaplumbağa oluşturma fonksiyonu
def create_turtle(color, shape):
    t = Turtle()
    t.penup()
    t.shape(shape)  # Şekil belirle
    t.color(color)  # Renk belirle
    t.speed(10)  # Hızını artır
    t.goto(randint(-200, 200), randint(-200, 200))  # Rastgele konum
    t.setheading(randint(0, 360))  # Rastgele yön belirle
    return t  # Yeni kaplumbağayı döndür

# Kaplumbağaya tıklandığında çalışacak fonksiyonlar
def on_click_t1(x, y):
    t1.write("BURDA!", align="center")
    new_x = randint(-200, 200)
    new_y = randint(-200, 200)
    t1.goto(new_x, new_y)
    t1.setheading(randint(0, 360))

def on_click_t2(x, y):
    t2.write("BURDA!", align="center")
    new_x = randint(-200, 200)
    new_y = randint(-200, 200)
    t2.goto(new_x, new_y)
    t2.setheading(randint(0, 360))

def on_click_t3(x, y):
    t3.write("BURDA!", align="center")
    new_x = randint(-200, 200)
    new_y = randint(-200, 200)
    t3.goto(new_x, new_y)
    t3.setheading(randint(0, 360))

# Kaplumbağaları oluştur
t1 = create_turtle("red", "turtle")
t2 = create_turtle("blue", "circle")
t3 = create_turtle("green", "triangle")

# Tıklama olaylarını bağla 
t1.onclick(on_click_t1)
t2.onclick(on_click_t2)
t3.onclick(on_click_t3)

# Kaplumbağaların ekranda olup olmadığını kontrol eden fonksiyon
def is_outside(turtle_obj):
    x, y = turtle_obj.xcor(), turtle_obj.ycor()
    if x > 230 or x < -230 or y > 230 or y < -230:
        return True
    return False

# Oyun döngüsü
def game_loop():
    while True:
        t1.forward(5)
        t2.forward(5)
        t3.forward(5)

        # Eğer kaplumbağa ekran dışına çıkarsa gizle
        if is_outside(t1):
            t1.hideturtle()
        if is_outside(t2):
            t2.hideturtle()
        if is_outside(t3):
            t3.hideturtle()

        # Eğer tüm kaplumbağalar gizlendiyse oyunu bitir
        if not t1.isvisible() and not t2.isvisible() and not t3.isvisible():
            break

        sleep(0.1)  # Oyun hızını kontrol etmek için

    # Kazanma mesajı
    t = Turtle()
    t.penup()
    t.hideturtle()
    t.goto(0, 0)
    t.write("KAYBETTIN!", align="center", font=("Arial", 16, "bold"))

# Oyunu başlat
game_loop()

# Ekranı açık tut
mainloop()
