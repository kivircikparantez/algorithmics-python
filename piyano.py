import play
import pygame

# Arka plan rengi
play.set_backdrop("white")

# Giriş Ekranı
baslik = play.new_text(words="Eğlenceli Piyano !", x=0, y=200)
aciklama = play.new_text(words="Melodi oluşturma için tuşlara tıkla",
                         x=0, y=150)
giris_yazisi = play.new_text(words="Yeteneklerini göstermeye hazırsan başlayalım :)"
                             ,x=0,y=240, font_size=25)
buton_baslat = play.new_box(color="light yellow", 
                            border_color="black", border_width=1,
                            x=-100, y=-170, width=160, height=50
                            )
yazi_baslat = play.new_text(words="başlat",
                             x=-20, y=-220, font_size=20)

buton_cal = play.new_box(color="light green", border_color="black",
                         border_width=1, x=-100, y=-170)

text_cal = play.new_text(words="melodiyi çal", x=-100, y=-170, font_size=20)

buton_temizle = play.new_box(color="light yellow", border_color="black",
                         border_width=1, x=100, y=-170)
text_temizle = play.new_text(words="melodiyi temizle", x=100, y=-170, 
                             font_size=20)

giris_resmi = play.new_image(image="giris.png",size=80)

# tuşlar ve sesler 
beyaz_tuslar = []
siyah_tuslar = []
nota_sesleri = []
kayitli_melodi = []

for i in range(8):
    x = -180 + i * 60
    tus = play.new_box(color="white", border_width=3, x=x, y=0, width=50,
                       height=100)
    beyaz_tuslar.append(tus)
    ses = pygame.mixer.Sound(str(i+1) + ".ogg")
    nota_sesleri.append(ses)

for i in range(8):
    x=-150 + i * 60
    tus= play.new_box(color="black", border_width=3, x=x, y=15, width=25, 
                      height=75)
    siyah_tuslar.append(tus)


# Nota isimlerini göster
def notalari_goster():
    notalar = ["DO", "RE", "Mİ", "FA", "SOL", "LA", "Sİ", "DO"]
    for i in range(8):
        x = -180 + i * 60
        play.new_text(words=notalar[i], x=x, y=0, font_size=25, color="white")

# başlangıçta gizlediklerimiz
@play.when_program_starts
def program_baslasin():
    pygame.mixer_music.load("1.ogg")
    pygame.mixer_music.play()
    baslik.hide()
    aciklama.hide()
    buton_cal.hide()
    text_cal.hide()
    buton_temizle.hide()
    text_temizle.hide()
    for tus in beyaz_tuslar:
        tus.hide()
    for tus in siyah_tuslar:
        tus.hide()

# Başlat butonuna basıldığında
@buton_baslat.when_clicked
def baslat_tiklandi():
    notalari_goster()
    baslik.show()
    aciklama.show()
    buton_cal.show()
    text_cal.show()
    buton_temizle.show()
    text_temizle.show()
    for tus in beyaz_tuslar:
        tus.show()
    for tus in siyah_tuslar:
        tus.show()
    buton_baslat.hide()
    yazi_baslat.hide()

# melodiyi çal
@buton_cal.when_clicked
async def melodiyi_cal():
    for index in kayitli_melodi:
        if 0 <= index < len(nota_sesleri):
            await play.timer(seconds=0.5)
            nota_sesleri[index].play()

@buton_temizle.when_clicked
def melodi_temizle():
    kayitli_melodi.clear()

