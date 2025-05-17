import pygame
import sys

pygame.init()

# Ekran ayarları
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sepet Toplama Oyunu")

# Renkler
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)

# Font
font = pygame.font.Font(None, 30)

# Fiyatlar ve KDV
fiyatlar = {"Muz": 10, "Elma": 5, "Armut": 6}
KDV_ORANI = 0.18

# Sepet
sepet = {}

# Kutuların pozisyon ve hareket bilgisi
kutular = {
    "Muz": {"rect": pygame.Rect(100, 50, 150, 100), "offset": 0, "is_moving": False},
    "Elma": {"rect": pygame.Rect(250, 50, 150, 100), "offset": 0, "is_moving": False},
    "Armut": {"rect": pygame.Rect(400, 50, 150, 100), "offset": 0, "is_moving": False},
}

# Hareket ayarları
max_kayma = 10
kayma_hiz = 2

clock = pygame.time.Clock()

def toplam_tutar_ve_kdv_hesapla():
    toplam = 0
    toplam_kdv = 0
    for urun, veri in sepet.items():
        adet = veri['adet']
        fiyat = veri['fiyat']
        toplam += fiyat * adet
        toplam_kdv += fiyat * KDV_ORANI * adet
    return toplam_kdv, toplam + toplam_kdv

# Ana döngü
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()

            for urun, veri in kutular.items():
                kutu = veri["rect"].copy()
                kutu.y += veri["offset"]  # Animasyonlu haliyle karşılaştır
                if kutu.collidepoint(mx, my):
                    # Sepete ekle
                    if urun not in sepet:
                        sepet[urun] = {"adet": 1, "fiyat": fiyatlar[urun]}
                    else:
                        sepet[urun]['adet'] += 1
                    # Hareketi başlat
                    veri["offset"] = 0
                    veri["is_moving"] = True

            # Sepetten çıkarma
            silinecekler = []
            for i, (urun, veri) in enumerate(sepet.items()):
                sepet_rect = pygame.Rect(10, 150 + i * 40, 200, 30)
                if sepet_rect.collidepoint(mx, my):
                    if veri["adet"] > 1:
                        sepet[urun]["adet"] -= 1
                    else:
                        silinecekler.append(urun)
            for urun in silinecekler:
                del sepet[urun]

    # Kutulara hareket uygula
    for urun, veri in kutular.items():
        if veri["is_moving"]:
            if veri["offset"] < max_kayma and not veri.get("returning", False):
                veri["offset"] += kayma_hiz
            else:
                veri["returning"] = True
                veri["offset"] -= kayma_hiz
                if veri["offset"] <= 0:
                    veri["offset"] = 0
                    veri["is_moving"] = False
                    veri["returning"] = False

    # Kutuları çiz
    for urun, veri in kutular.items():
        rect = veri["rect"]
        offset = veri["offset"]
        kutu_rect = pygame.Rect(rect.x, rect.y + offset, rect.width, rect.height)
        renk = RED if urun == "Muz" else GREEN if urun == "Elma" else BLUE
        pygame.draw.rect(screen, renk, kutu_rect)
        text = font.render(f"{urun}: {fiyatlar[urun]} TL", True, TEXT_COLOR)
        screen.blit(text, (kutu_rect.centerx - text.get_width() / 2, kutu_rect.centery - text.get_height() / 2))

    # Sepet bilgisi
    y = 150
    for urun, veri in sepet.items():
        sepet_text = font.render(f"{urun} x{veri['adet']} - {veri['fiyat']} TL", True, BLACK)
        screen.blit(sepet_text, (10, y))
        y += 40

    toplam_kdv, toplam_fiyat = toplam_tutar_ve_kdv_hesapla()
    toplam_text = font.render(f"Toplam KDV: {toplam_kdv:.2f} TL | Toplam Fiyat: {toplam_fiyat:.2f} TL", True, BLACK)
    screen.blit(toplam_text, (SCREEN_WIDTH // 2 - toplam_text.get_width() // 2, SCREEN_HEIGHT - 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
