import play
import random

# Ekran boyutları
GENISLIK, YUKSEKLIK = 800, 600
play.set_backdrop('black')

# Paddle ve Top nesneleri
paddle = play.new_image("platform.png", size=10, y=-250)
top = play.new_circle(color='yellow', x=0, y=0, radius=10)

# Tuğlalar
tuğla_sayisi_x = 7
tuğla_sayisi_y = 5
tuğla_genislik = 75
tuğla_yukseklik = 20
tuğla_renkleri = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple', 'pink', 'lime']
tuğlalar = []

for i in range(tuğla_sayisi_x):
    for j in range(tuğla_sayisi_y):
        x_koordinati = -300 + i * 100
        y_koordinati = 200 - j * 40
        renk = random.choice(tuğla_renkleri)
        tuğla = play.new_box(color=renk, width=tuğla_genislik, height=tuğla_yukseklik, x=x_koordinati, y=y_koordinati)
        tuğlalar.append(tuğla)

# Topun hızı
top_hiz_x = 3
top_hiz_y = -3

# Oyun durumu
oyun_bitti = False
oyun_kazandı = False

# Oyun kazandı ve kaybetti yazıları
kazandın_yazısı = play.new_text(words="Kazandın!", x=0, y=0, font_size=50, color='green')
kaybettin_yazısı = play.new_text(words="Kaybettin!", x=0, y=0, font_size=50, color='red')

# Yeniden başlat düğmesi
yeniden_baslat_dugmesi = play.new_text(words="Yeniden Başlat", x=0, y=-50, font_size=30, color='yellow')

# Başlangıçta yazıları ve düğmeyi gizle
kazandın_yazısı.hide()
kaybettin_yazısı.hide()
yeniden_baslat_dugmesi.hide()

# Işık efekti fonksiyonu
def ışık_efekti(x, y):
    ışık = play.new_circle(color='white', x=x, y=y, radius=5, transparency=0)

    büyüme_adımı = 0

    @play.repeat_forever
    async def büyüt_ve_yoket():
        nonlocal büyüme_adımı
        büyüme_adımı += 1
        ışık.radius += 2
        ışık.transparency += 10
        if büyüme_adımı > 10:
            ışık.remove()
            büyüt_ve_yoket.stop()
        await play.timer(0.03)

# Oyunu yeniden başlatma fonksiyonu
def oyunu_yeniden_baslat():
    global paddle, top, tuğlalar, top_hiz_x, top_hiz_y, oyun_bitti, oyun_kazandı

    paddle.x, paddle.y = 0, -250
    top.x, top.y = 0, 0
    top_hiz_x, top_hiz_y = 3, -3
    oyun_bitti, oyun_kazandı = False, False

    kazandın_yazısı.hide()
    kaybettin_yazısı.hide()
    yeniden_baslat_dugmesi.hide()

    # Mevcut tuğlaları sahneden kaldır
    for tuğla in tuğlalar:
        tuğla.remove()

    # Tuğlalar listesini sıfırla
    tuğlalar.clear()

    # Yeni tuğlaları oluştur
    for i in range(tuğla_sayisi_x):
        for j in range(tuğla_sayisi_y):
            x_koordinati = -300 + i * 100
            y_koordinati = 200 - j * 40
            renk = random.choice(tuğla_renkleri)
            yeni_tuğla = play.new_box(color=renk, width=tuğla_genislik, height=tuğla_yukseklik, x=x_koordinati, y=y_koordinati)
            tuğlalar.append(yeni_tuğla)

@play.repeat_forever
def oyun_dongusu():
    global top_hiz_x, top_hiz_y, oyun_bitti, oyun_kazandı

    if oyun_bitti or oyun_kazandı:
        return

    # Paddle hareketi
    if play.key_is_pressed('left') and paddle.x > -GENISLIK / 2 + paddle.width / 2:
        paddle.x -= 10
    if play.key_is_pressed('right') and paddle.x < GENISLIK / 2 - paddle.width / 2:
        paddle.x += 10

    # Top hareketi
    top.x += top_hiz_x
    top.y += top_hiz_y

    # Ekran kenarlarına çarpma
    if top.x >= GENISLIK / 2 - top.radius or top.x <= -GENISLIK / 2 + top.radius:
        top_hiz_x = -top_hiz_x
    if top.y >= YUKSEKLIK / 2 - top.radius:
        top_hiz_y = -top_hiz_y

    # Paddle'a çarpma
    if paddle.is_touching(top):
        top_hiz_y = -top_hiz_y

    # Tuğlalara çarpma
    for tuğla in tuğlalar:
        if tuğla.is_touching(top):
            top_hiz_y = -top_hiz_y
            ışık_efekti(tuğla.x, tuğla.y)
            tuğla.hide()
            tuğlalar.remove(tuğla)
            break

    # Kazanma durumu
    if not tuğlalar:
        oyun_kazandı = True
        kazandın_yazısı.show()
        yeniden_baslat_dugmesi.show()

    # Kaybetme durumu
    if top.y <= -YUKSEKLIK / 2 + top.radius and not oyun_kazandı:
        oyun_bitti = True
        kaybettin_yazısı.show()
        yeniden_baslat_dugmesi.show()

@yeniden_baslat_dugmesi.when_clicked
def yeniden_baslat_tiklandi():
    oyunu_yeniden_baslat()

play.start_program()
