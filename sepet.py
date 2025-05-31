import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("🛒 Scroll'lu Sepet Uygulaması")

font = pygame.font.SysFont("Arial", 24)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
KDV_ORANI = 0.20
clock = pygame.time.Clock()

urunler = [
    {"isim": "Elma", "fiyat": 3, "color": (255, 100, 100), "rect": pygame.Rect(50, 50, 150, 80)},
    {"isim": "Muz", "fiyat": 5, "color": (255, 255, 100), "rect": pygame.Rect(225, 50, 150, 80)},
    {"isim": "Çilek", "fiyat": 7, "color": (255, 150, 200), "rect": pygame.Rect(400, 50, 150, 80)},
]

sepet = []
sepet_rects = []

# Scroll için
scroll_offset = 0
max_scroll = 0

# Animasyon
animating = False
anim_urun = None
anim_pos = [0, 0]
anim_target = (50, 200)

def draw_products():
    for urun in urunler:
        pygame.draw.rect(screen, urun["color"], urun["rect"])
        pygame.draw.rect(screen, BLACK, urun["rect"], 2)
        text = font.render(f"{urun['isim']} - {urun['fiyat']} TL", True, BLACK)
        screen.blit(text, (urun["rect"].x + 10, urun["rect"].y + 25))

def draw_cart():
    global sepet_rects, max_scroll
    sepet_rects = []
    y_start = 220 + scroll_offset
    screen.blit(font.render("Sepettekiler (Silmek için tıkla):", True, BLACK), (50, 190))

    for i, item in enumerate(sepet):
        y = y_start + i * 30
        text = font.render(f"{item['isim']} - {item['fiyat']} TL", True, BLACK)
        rect = text.get_rect(topleft=(50, y))
        sepet_rects.append((rect, item))
        if 200 <= y <= 370:  # görünür alan sınırı
            screen.blit(text, rect)

    max_scroll = max(0, len(sepet) * 30 - 170)  # 170px'lik görünür alan

def draw_total():
    toplam = sum(item["fiyat"] for item in sepet)
    kdv = toplam * KDV_ORANI
    toplam_kdv = toplam + kdv
    y = 400
    screen.blit(font.render(f"Ara Toplam: {toplam:.2f} TL", True, BLACK), (50, y))
    screen.blit(font.render(f"KDV (%20): {kdv:.2f} TL", True, BLACK), (50, y + 30))
    screen.blit(font.render(f"Toplam (KDV Dahil): {toplam_kdv:.2f} TL", True, BLACK), (50, y + 60))

def start_animation(urun):
    global animating, anim_urun, anim_pos
    animating = True
    anim_urun = urun
    anim_pos = [urun["rect"].x, urun["rect"].y]

def update_animation():
    global animating
    if not animating:
        return

    speed = 10
    dx = anim_target[0] - anim_pos[0]
    dy = anim_target[1] - anim_pos[1]
    distance = (dx ** 2 + dy ** 2) ** 0.5

    if distance < 10:
        animating = False
        sepet.append(anim_urun)
    else:
        anim_pos[0] += dx / distance * speed
        anim_pos[1] += dy / distance * speed
        pygame.draw.rect(screen, anim_urun["color"], (anim_pos[0], anim_pos[1], 150, 80))
        pygame.draw.rect(screen, BLACK, (anim_pos[0], anim_pos[1], 150, 80), 2)

# Ana döngü
while True:
    screen.fill(WHITE)
    draw_products()
    draw_cart()
    draw_total()
    update_animation()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            # Ürün ekleme (animasyonla)
            if not animating:
                for urun in urunler:
                    if urun["rect"].collidepoint(pos):
                        start_animation(urun)

            # Sepetteki ürüne tıklayıp silme
            for rect, item in sepet_rects:
                if rect.collidepoint(pos):
                    sepet.remove(item)
                    break

        elif event.type == pygame.MOUSEWHEEL:
            scroll_offset += event.y * 20  # scroll up/down
            scroll_offset = max(-max_scroll, min(0, scroll_offset))

    pygame.display.flip()
    clock.tick(60)
