import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alışveriş Sepeti App")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)
RED = (200, 50, 50)

font = pygame.font.SysFont("Arial", 22)

products = [
    {"name": "Elma", "price": 5},
    {"name": "Erik", "price": 8},
    {"name": "Süt", "price": 10},
    {"name": "Peynir", "price": 15},
    {"name": "Makarna", "price": 6},
    {"name": "Mandalina", "price": 9},
    {"name": "Portakal", "price": 7},
]

cart = []
cart_item_rects = []

product_scroll_x = 0
cart_scroll = 0

animated_items = []  # {"product": ..., "y": ..., "target_y": ...}

def draw_product_list():
    global product_scroll_x

    product_area_height = 150
    item_width = 140
    item_height = 50
    spacing = 20
    surface_width = len(products) * (item_width + spacing) + 20

    product_surface = pygame.Surface((surface_width, product_area_height))
    product_surface.fill(WHITE)

    x = 10
    y = 40
    for product in products:
        rect = pygame.Rect(x, y, item_width, item_height)
        pygame.draw.rect(product_surface, GRAY, rect)

        text = font.render(f"{product['name']}", True, BLACK)
        price = font.render(f"{product['price']}₺", True, BLACK)

        text_rect = text.get_rect(center=(rect.centerx, rect.centery - 8))
        price_rect = price.get_rect(center=(rect.centerx, rect.centery + 12))

        product_surface.blit(text, text_rect)
        product_surface.blit(price, price_rect)

        product['rect'] = pygame.Rect(rect.x - product_scroll_x, rect.y, rect.width, rect.height)

        x += item_width + spacing

    max_scroll = max(0, surface_width - WIDTH)
    product_scroll_x = max(0, min(product_scroll_x, max_scroll))

    screen.blit(product_surface, (0, 0), area=pygame.Rect(product_scroll_x, 0, WIDTH, product_area_height))


def draw_cart():
    global cart_scroll, cart_item_rects
    cart_item_rects = []

    cart_area_y = 150
    cart_area_height = HEIGHT - cart_area_y - 50
    cart_surface_height = max(cart_area_height, len(cart) * 30 + 60)

    cart_surface = pygame.Surface((WIDTH, cart_surface_height))
    cart_surface.fill((230, 230, 230))

    cart_surface.blit(font.render("Sepetiniz:", True, BLACK), (30, 10))

    y = 40
    total = 0
    for i, item in enumerate(cart):
        text = font.render(f"{item['name']} - {item['price']}₺", True, BLACK)
        text_rect = cart_surface.blit(text, (40, y))
        cart_item_rects.append({"rect": pygame.Rect(text_rect.x, y + cart_scroll, text_rect.width, text_rect.height), "index": i})
        y += 30
        total += item["price"]

    max_scroll = max(0, cart_surface_height - cart_area_height)
    cart_scroll = max(0, min(cart_scroll, max_scroll))

    screen.blit(cart_surface, (0, cart_area_y), area=pygame.Rect(0, cart_scroll, WIDTH, cart_area_height))

    pygame.draw.rect(screen, (200, 255, 200), (0, HEIGHT - 50, WIDTH, 50))
    total_text = font.render(f"Toplam Tutar: {total}₺", True, GREEN)
    screen.blit(total_text, (WIDTH - 250, HEIGHT - 40))


def draw_clear_button():
    button_rect = pygame.Rect(WIDTH - 170, 5, 160, 35)  # Butonun pozisyonunu yukarıya çektik
    pygame.draw.rect(screen, RED, button_rect)
    text = font.render("Hepsini Temizle", True, WHITE)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
    return button_rect

def handle_animations():
    finished = []
    for anim in animated_items:
        anim["y"] += 10
        product = anim["product"]
        rect = pygame.Rect(200, anim["y"], 140, 50)
        pygame.draw.rect(screen, GRAY, rect)
        text = font.render(product["name"], True, BLACK)
        price = font.render(f"{product['price']}₺", True, BLACK)
        screen.blit(text, (rect.x + 10, rect.y + 5))
        screen.blit(price, (rect.x + 10, rect.y + 25))
        if anim["y"] >= anim["target_y"]:
            finished.append(anim)

    for anim in finished:
        cart.append(anim["product"])
        animated_items.remove(anim)

def check_click(pos):
    # Hepsini Temizle butonu
    if clear_button.collidepoint(pos):
        cart.clear()
        return

    # Ürünlere tıklama: Silme işlemi kaldırıldı, sadece sepete ekleme yapılacak
    for product in products:
        if product.get('rect') and product['rect'].collidepoint(pos):
            animated_items.append({
                "product": product,
                "y": 50,
                "target_y": 160  # Sepet alanının başlangıcı
            })
            break

# Ana döngü
running = True
while running:
    screen.fill(WHITE)

    draw_product_list()
    draw_cart()
    clear_button = draw_clear_button()
    handle_animations()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                check_click(event.pos)
            elif event.button == 4:
                if event.pos[1] < 150:
                    product_scroll_x -= 30
                else:
                    cart_scroll -= 20
            elif event.button == 5:
                if event.pos[1] < 150:
                    product_scroll_x += 30
                else:
                    cart_scroll += 20

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                product_scroll_x -= 30
            elif event.key == pygame.K_RIGHT:
                product_scroll_x += 30
            elif event.key == pygame.K_UP:
                cart_scroll -= 20
            elif event.key == pygame.K_DOWN:
                cart_scroll += 20

    pygame.display.flip()
    clock.tick(60)
