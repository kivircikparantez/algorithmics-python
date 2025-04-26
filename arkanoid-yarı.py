import play 
import random 

GENISLIK, YUKSEKLIK = 800, 600
play.set_backdrop("black")

# paddle ve top nesnelerini 
paddle = play.new_box(color= "green", width = 100, height=30, y=-250)
top = play.new_circle(color="yellow", x=0, y=0, radius=10)

tugla_sayisi_x = 7
tugla_sayisi_y = 5
tugla_genisligi = 75
tugla_yuksekligi = 20
tugla_renkleri = ["red", "orange", "yellow", "green", "cyan",
                   "blue", "purple","pink","lime"]
tuglalar = []

for i in range(tugla_sayisi_x):
    for j in range(tugla_sayisi_y):
        print(i,j)
        x_koordinati = -300 + i * 100
        y_koordinati = 200 - j * 40
        renk = random.choice(tugla_renkleri)
        tugla = play.new_box(color= renk , width= tugla_genisligi,
                             height=tugla_yuksekligi, x= x_koordinati, 
                             y=y_koordinati)
        tuglalar.append(tugla)


# topun hızı
top_hiz_x = 3
top_hiz_y = -3

# oyun durumu

oyun_bitti = False
oyun_kazandi = False

kazandin_yazisi = play.new_text(words = "Kazandın", x=0, y=0,
                                font_size=50, color="green")
kaybettin_yazisi = play.new_text(words = "Kaybettin", x=0, y=0,
                                font_size=50, color="red")
yeniden_baslat_yazisi = play.new_text(words = "Yeniden Başlat", x=0, y=-50,
                                font_size=50, color="yellow")

kazandin_yazisi.hide()
kaybettin_yazisi.hide()
yeniden_baslat_yazisi.hide()

@play.repeat_forever
def oyun_dongusu():
    global top_hiz_x, top_hiz_y, oyun_bitti, oyun_kazandi
    if oyun_bitti or oyun_kazandi:
        return

    # paddle hareketi
    if play.key_is_pressed("left") and paddle.x >  -GENISLIK/2 + paddle.width /2:
        paddle.x -= 10
    if play.key_is_pressed("right") and paddle.x >  GENISLIK/2 - paddle.width /2:
        paddle.x += 10
        

play.start_program()
