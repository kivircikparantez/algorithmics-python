import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Basit Market')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CATEGORY_COLORS = [(100, 200, 100), (255, 180, 80), (255, 220, 100)]

font = pygame.font.SysFont('Arial', 24)
title_font = pygame.font.SysFont('Arial', 36)

categories = ["Sebze & Meyve", "Fast Food", "Kahvaltılıklar"]

products = {
    "Sebze & Meyve": [{"name": "Elma", "price": 3}, {"name": "Muz", "price": 2}, {"name": "Armut", "price": 4}],
    "Fast Food": [{"name": "Hamburger", "price": 10}, {"name": "Patates", "price": 5}, {"name": "Kola", "price": 3}],
    "Kahvaltılıklar": [{"name": "Süt", "price": 2.5}, {"name": "Ekmek", "price": 1.5}, {"name": "Yumurta", "price": 3}]
}

# Kategori ikonlarını yükle
icons = {
    "Sebze & Meyve": pygame.transform.scale(pygame.image.load("ikon_sebze.png"), (60, 60)),
    "Fast Food": pygame.transform.scale(pygame.image.load("ikon_fastfood.png"), (60, 60)),
    "Kahvaltılıklar": pygame.transform.scale(pygame.image.load("ikon_kahvalti.png"), (60, 60))
}

def load_image(image_path):
    try:
        return pygame.image.load(image_path)
    except:
        return None

def draw_start_screen(mouse_pos):
    bg = load_image("giris_ekrani.png")
    if bg:
        bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
        screen.blit(bg, (0, 0))
    else:
        screen.fill(WHITE)

    buttons = []
    box_width = 200
    box_height = 150
    spacing = 50
    start_x = (WIDTH - (box_width * len(categories) + spacing * (len(categories) - 1))) // 2
    y = 400

    for i, cat in enumerate(categories):
        x = start_x + i * (box_width + spacing)
        rect = pygame.Rect(x, y, box_width, box_height)

        is_hover = rect.collidepoint(mouse_pos)
        grow = 10 if is_hover else 0
        display_rect = pygame.Rect(x - grow // 2, y - grow // 2, box_width + grow, box_height + grow)

        color = CATEGORY_COLORS[i]
        pygame.draw.rect(screen, color, display_rect, border_radius=15)

        border_thickness = 4 if is_hover else 2
        pygame.draw.rect(screen, BLACK, display_rect, border_thickness, border_radius=15)

        # İkonu çiz
        icon = icons[cat]
        icon_x = display_rect.centerx - icon.get_width() // 2
        icon_y = display_rect.y + 10
        screen.blit(icon, (icon_x, icon_y))

        # Metni çiz
        text_surface = font.render(cat, True, BLACK)
        screen.blit(text_surface, (
            display_rect.centerx - text_surface.get_width() // 2,
            display_rect.bottom - text_surface.get_height() - 10
        ))

        buttons.append((rect, cat))

    return buttons

def draw_product_screen(category):
    screen.fill(WHITE)
    category_text = title_font.render(f"{category} Ürünleri", True, BLACK)
    screen.blit(category_text, (WIDTH // 2 - category_text.get_width() // 2, 50))

    y_offset = 150
    for product in products[category]:
        product_text = f"{product['name']} - ${product['price']}"
        text_surface = font.render(product_text, True, BLACK)
        screen.blit(text_surface, (50, y_offset))
        y_offset += 40

clock = pygame.time.Clock()
current_screen = "start"
selected_category = None

while True:
    mouse_pos = pygame.mouse.get_pos()
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "start":
                for rect, cat in draw_start_screen(mouse_pos):
                    if rect.collidepoint(mouse_pos):
                        selected_category = cat
                        current_screen = "products"

    if current_screen == "start":
        draw_start_screen(mouse_pos)
    elif current_screen == "products" and selected_category:
        draw_product_screen(selected_category)

    pygame.display.flip()
    clock.tick(60)
    
    
    
    
    Harika! Kodun içine bu ikonları zaten ekledik. Şimdi bu ikonların oyun klasöründe doğru şekilde yer aldığından emin olman gerekiyor.

✅ Yapman Gerekenler:
Bu üç resmi proje klasörünün içine koy:

ikon_sebze.png

ikon_fastfood.png

ikon_kahvalti.png

Bu resimlerin isimleri tam olarak kodda geçtiği gibi olmalı (büyük-küçük harf dahil):

ikon_sebze.png

ikon_fastfood.png

ikon_kahvalti.png

Dosyalar .py dosyasının bulunduğu dizinde olmalı. Eğer farklı bir klasördeyse, kodda yolunu şöyle belirtmelisin:

piton

Kopyala

Düzenle
pygame.image.load("img/ikon_sebze.png")  # örnek
