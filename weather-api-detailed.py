import pygame
import requests

# Başlat
pygame.init()

# Pencere ayarı
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Detaylı Hava Durumu")

# Font ve renk
WHITE = (255, 255, 255)
GRAY = (240, 240, 240)
BLACK = (0, 0, 0)
font = pygame.font.SysFont("arial", 24)

# Giriş kutusu
input_box = pygame.Rect(250, 40, 300, 40)
user_text = ''
hava_bilgi = []
aktif_sehir = ''

clock = pygame.time.Clock()
running = True

def hava_detayli_getir(sehir):
    try:
        url = f"https://wttr.in/{sehir}?format=j1"
        response = requests.get(url)
        data = response.json()

        detaylar = []
        today = data['weather'][0]
        current = data['current_condition'][0]

        tarih = today['date']
        durum = current['weatherDesc'][0]['value']
        sicaklik = current['temp_C']
        nem = current['humidity']
        max_gun = today['maxtempC']
        min_gun = today['mintempC']

        detaylar.append(f"{sehir.title()} - {tarih}")
        detaylar.append(f"Durum: {durum}")
        detaylar.append(f"Sıcaklık: {sicaklik}°C")
        detaylar.append(f"Maks: {max_gun}°C  Min: {min_gun}°C")
        detaylar.append(f"Nem: %{nem}")
        return detaylar

    except Exception as e:
        return [f"Hata: {str(e)}"]

while running:
    screen.fill(WHITE)

    # Giriş kutusu
    pygame.draw.rect(screen, GRAY, input_box, border_radius=5)
    input_surface = font.render(user_text, True, BLACK)
    screen.blit(input_surface, (input_box.x + 10, input_box.y + 5))

    # Hava durumu kartı
    if hava_bilgi:
        pygame.draw.rect(screen, GRAY, pygame.Rect(100, 110, 600, 220), border_radius=10)
        for i, satir in enumerate(hava_bilgi):
            bilgi_surface = font.render(satir, True, BLACK)
            screen.blit(bilgi_surface, (120, 130 + i * 35))

    # Etkileşimler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                hava_bilgi = hava_detayli_getir(user_text)
                aktif_sehir = user_text
                user_text = ''
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
