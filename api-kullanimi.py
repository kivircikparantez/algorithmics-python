import pygame
import requests
from datetime import datetime

# Pygame başlat
pygame.init()

# Ekran ayarları
WIDTH, HEIGHT = 750, 350
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tarihli Emoji Hava Durumu")

# Renk ve font
WHITE = (255, 255, 255)
GRAY = (230, 230, 230)
BLACK = (10, 10, 10)
font = pygame.font.SysFont("arial", 28)

# Giriş kutusu
input_box = pygame.Rect(200, 50, 300, 40)
user_text = ''
hava_durumu = ''
tarih_bilgisi = ''

clock = pygame.time.Clock()
running = True

def hava_sorgula(sehir):
    try:
        # wttr.in sade emoji formatı
        url = f"https://wttr.in/{sehir}?format=3"
        cevap = requests.get(url)
        if cevap.status_code == 200:
            tarih = datetime.today().strftime('%Y-%m-%d')  # Günün tarihi
            return f"{tarih} - {cevap.text}"
        else:
            return "Veri alınamadı."
    except:
        return "Bağlantı hatası."

while running:
    screen.fill(WHITE)

    # Giriş kutusu çiz
    pygame.draw.rect(screen, GRAY, input_box, border_radius=5)
    text_surface = font.render(user_text, True, BLACK)
    screen.blit(text_surface, (input_box.x + 10, input_box.y + 5))

    # Hava durumu yazısı (tarihli)
    sonuc_surface = font.render(hava_durumu, True, BLACK)
    screen.blit(sonuc_surface, (50, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                hava_durumu = hava_sorgula(user_text)
                user_text = ''
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
