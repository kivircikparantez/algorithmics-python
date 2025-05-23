import play
from random import randint

arkaplan = play.new_image("GirisEkrani.jpg")
arkaplan.go_to(0,80)

GirisButton = play.new_box(color="red", x=0, y=-150, width=150, height=50, border_color="black", border_width=2)
GirisText = play.new_text(words ="Oyuna Başla", x = 0, y=-150, font=None, font_size=25, color="white")
CikisButton = play.new_image(image="Cikis.png", x=-350, y=-250, size=15)

ayarlar = play.new_image("Settings.png", x = 350, y=-250, size=12)
ayarlarBox = play.new_box(color="white", x=0, y=-250, width=500, height=60, border_color="red", border_width=6)
ayarlarText = play.new_text(words="Oyunu kazanmak için kırmızı başlıklı kızı hedefe ulaştıralım!", 
                            x= 0 , y = -250, font=None, font_size=22, color="black")
ayarlarBox.hide()
ayarlarText.hide()

oyunArkaPlan = play.new_image("wall.jpg", size=140, transparency=70)

kurt1 = play.new_image(image="kurt.png", x=-60, y=-195, size = 15)
kurt2 = play.new_image(image="kurt.png", x=-0, y=85, size = 15)
kurt3 = play.new_image(image="kurt.png", x=60, y=-15, size = 15)

kurt1.hide()
kurt2.hide() 
kurt3.hide() 

wall1 = play.new_box(color='black', x=300, y=20, width=10, height=400, border_color='white', border_width=2)
wall2 = play.new_box(color='black', x=0, y=-230, width=580, height=10, border_color='white', border_width=2)
wall3 = play.new_box(color='black', x=5, y=225, width=600, height=10, border_color='white', border_width=2)
wall4 = play.new_box(color='black', x=-295, y=-35, width=10, height=400, border_color='white', border_width=2)
wall5 = play.new_box(color='black', x=250, y=95, width=10, height=250, border_color='white', border_width=2)
wall6 = play.new_box(color='black', x=150, y=0, width=10, height=250, border_color='white', border_width=2)
wall7 = play.new_box(color='black', x=45, y=50, width=200, height=10, border_color='white', border_width=2)
wall8 = play.new_box(color='black', x=-100, y=150, width=200, height=10, border_color='white', border_width=2)
wall9 = play.new_box(color='black', x=245, y=-100, width=100, height=10, border_color='white', border_width=2)
wall10 = play.new_box(color='black', x=-150, y=-100, width=100, height=10, border_color='white', border_width=2)
wall11 = play.new_box(color='black', x=100, y=-175, width=10, height=100, border_color='white', border_width=2)
wall12 = play.new_box(color='black', x=-95, y=-145, width=10, height=100, border_color='white', border_width=2)
wall13 = play.new_box(color='black', x=45, y=-130, width=100, height=10, border_color='white', border_width=2)
wall14 = play.new_box(color='black', x=-50, y=-50, width=100, height=10, border_color='white', border_width=2)
wall15 = play.new_box(color='black', x=-205, y=-125, width=10, height=200, border_color='white', border_width=2)
wall16 = play.new_box(color='black', x=-250, y=50, width=10, height=100, border_color='white', border_width=2)
wall17 = play.new_box(color='black', x=5, y=170, width=10, height=100, border_color='white', border_width=2)
wall18 = play.new_box(color='black', x=5, y=-40, width=10, height=100, border_color='white', border_width=2)
wall19 = play.new_box(color='black', x=95, y=-50, width=100, height=10, border_color='white', border_width=2)
wall20 = play.new_box(color='black', x=-205, y=105, width=100, height=10, border_color='white', border_width=2)
wall21 = play.new_box(color='black', x=-110, y=95, width=10, height=100, border_color='white', border_width=2)
wall22 = play.new_box(color='black', x=50, y=125, width=80, height=10, border_color='white', border_width=2)
wall23 = play.new_box(color='black', x=220, y=60, width=50, height=10, border_color='white', border_width=2)

anaKarakter = play.new_image(image="AnaKarakter.png", x=280, y=-200, size=7)
anaKarakter.hide()

ormanEvi = play.new_image(image="ev.png", x=-305, y=198, size=15)
ormanEvi.hide()

konfeti_parcalari = []

def konfeti_patlat(x,y):
    konfeti = play.new_circle("yellow", x=x, y=y, radius=5)
    konfeti_parcalari.append(konfeti)

@ayarlar.when_clicked
async def settings():
    ayarlarBox.show()
    ayarlarText.show()
    await play.timer(seconds=4)
    ayarlarText.words = "Labirentteki kurtlaara dikkat etmeniz gerekmektedir!"
    await play.timer(seconds=4)
    ayarlarBox.hide()
    ayarlarText.hide()
    ayarlarText.words = "Oyunu kazanmak için kırmızı başlıklı kızı hedefe ulaştıralım!"

@CikisButton.when_clicked
async def cikis():
    await play.timer(seconds=1)
    quit()

@GirisButton.when_clicked
async def giris():
    arkaplan.hide()
    GirisButton.hide()
    GirisText.hide()
    CikisButton.hide()
    ayarlar.hide()
    ayarlarBox.hide()
    ayarlarText.hide()
    anaKarakter.show()
    ormanEvi.show()
    kurt1.show()
    kurt2.show()
    kurt3.show()
    wall1.show()
    wall2.show()
    wall3.show()
    wall4.show()
    wall5.show()
    wall6.show()
    wall7.show()
    wall8.show()
    wall9.show()
    wall10.show()
    wall11.show()
    wall12.show()
    wall13.show()
    wall14.show()
    wall15.show()
    wall16.show()
    wall17.show()
    wall18.show()
    wall19.show()
    wall20.show()
    wall21.show()
    wall22.show()
    wall23.show()
    oyunArkaPlan.show()

@play.when_program_starts
async def start():
    wall1.hide()
    wall2.hide()
    wall3.hide()
    wall4.hide()
    wall5.hide()
    wall6.hide()
    wall7.hide()
    wall8.hide()
    wall9.hide()
    wall10.hide()
    wall11.hide()
    wall12.hide()
    wall13.hide()
    wall14.hide()
    wall15.hide()
    wall16.hide()
    wall17.hide()
    wall18.hide()
    wall19.hide()
    wall20.hide()
    wall21.hide()
    wall22.hide()
    wall23.hide()
    oyunArkaPlan.hide()
    anaKarakter.start_physics(bounciness=5, friction=2)
    ormanEvi.start_physics(can_move=False)
    kurt1.start_physics()
    kurt2.start_physics()
    kurt3.start_physics()
    wall1.start_physics(can_move=False)
    wall2.start_physics(can_move=False)
    wall3.start_physics(can_move=False)
    wall4.start_physics(can_move=False)
    wall5.start_physics(can_move=False)
    wall6.start_physics(can_move=False)
    wall7.start_physics(can_move=False)
    wall8.start_physics(can_move=False)
    wall9.start_physics(can_move=False)
    wall10.start_physics(can_move=False)
    wall11.start_physics(can_move=False)
    wall12.start_physics(can_move=False)
    wall13.start_physics(can_move=False)
    wall14.start_physics(can_move=False)
    wall15.start_physics(can_move=False)
    wall16.start_physics(can_move=False)
    wall17.start_physics(can_move=False)
    wall18.start_physics(can_move=False)
    wall19.start_physics(can_move=False)
    wall20.start_physics(can_move=False)
    wall21.start_physics(can_move=False)
    wall22.start_physics(can_move=False)
    wall23.start_physics(can_move=False)

@play.repeat_forever
async def game():
    anaKarakter.x_speed = 0
    anaKarakter.y_speed = 0
    if play.key_is_pressed("w","up"):
        anaKarakter.physics.y_speed = 15
    if play.key_is_pressed("s","down"):
        anaKarakter.physics.y_speed = -15
    if play.key_is_pressed("d","right"):
        anaKarakter.physics.x_speed = 15 
    if play.key_is_pressed("a","left"):
        anaKarakter.physics.x_speed = -15
    if anaKarakter.is_touching(ormanEvi):
        wall1.hide()
        wall2.hide()
        wall3.hide()
        wall4.hide()
        wall5.hide()
        wall6.hide()
        wall7.hide()
        wall8.hide()
        wall9.hide()
        wall10.hide()
        wall11.hide()
        wall12.hide()
        wall13.hide()
        wall14.hide()
        wall15.hide()
        wall16.hide()
        wall17.hide()
        wall18.hide()
        wall19.hide()
        wall20.hide()
        wall21.hide()
        wall22.hide()
        wall23.hide()
        oyunArkaPlan.hide()
        anaKarakter.hide()
        ormanEvi.hide()
        kurt1.hide()
        kurt2.hide()
        kurt3.hide()
        for parca in konfeti_parcalari:
            parca.hide()
        konfeti_parcalari.clear()
        for _ in range(50):
            konfeti_patlat(play.random_number(-play.screen.width /2 , play.screen.width/2),
                            play.random_number(-play.screen.height /2 , play.screen.height/2))
        play.new_text(words="Tebrikler! Kurtlardan kurtuldun ve eve ulaştın.. ", 
                      x=0, y=0,font_size=50,color="green")
        await play.timer(seconds=5)
    await play.timer(seconds=1/60)
    
@play.repeat_forever
async def move_kurt1():
    kurt1.physics.x_speed = 5  
    if kurt1.x < -50:
        kurt1.direction = "right"
    if kurt1.x > 50:
        kurt1.direction = "left"
    if kurt1.direction == "left":
        kurt1.x -= randint(1,10)  
    else: 
        kurt1.x += randint(1,10)
    await play.timer(seconds=1/60)

@play.repeat_forever
async def move_kurt2():
    kurt2.physics.x_speed = 5  
    if kurt2.x < 15:
        kurt2.direction = "right"
    if kurt2.x > 80:
        kurt2.direction = "left"
    if kurt2.direction == "left":
        kurt2.x -= randint(1,5)  
    else: 
        kurt2.x += randint(1,5)
    await play.timer(seconds=1/60)

@play.repeat_forever
async def move_kurt3():
    kurt3.physics.x_speed = 5  
    if kurt3.x < 15:
        kurt3.direction = "right"
    if kurt3.x > 80:
        kurt3.direction = "left"
    if kurt3.direction == "left":
        kurt3.x -= randint(1,5)  
    else: 
        kurt3.x += randint(1,5)
    await play.timer(seconds=1/60)

@play.repeat_forever
async def game_over():
    if anaKarakter.is_touching(kurt1) or anaKarakter.is_touching(kurt2) or anaKarakter.is_touching(kurt3):
        wall1.hide()
        wall2.hide()
        wall3.hide()
        wall4.hide()
        wall5.hide()
        wall6.hide()
        wall7.hide()
        wall8.hide()
        wall9.hide()
        wall10.hide()
        wall11.hide()
        wall12.hide()
        wall13.hide()
        wall14.hide()
        wall15.hide()
        wall16.hide()
        wall17.hide()
        wall18.hide()
        wall19.hide()
        wall20.hide()
        wall21.hide()
        wall22.hide()
        wall23.hide()
        oyunArkaPlan.hide()
        anaKarakter.hide()
        ormanEvi.hide()
        kurt1.hide()
        kurt2.hide()
        kurt3.hide()
        play.new_text(words ="Oyun Bitti! Kaybettin ... ", x=0, y=0,  font_size=50, color="red")
        await play.timer(seconds=5)
    await play.timer(seconds=1/60)
play.start_program ()
