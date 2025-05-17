import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alışveriş Sepeti App")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)
RED = (200, 50, 50)
LIGHT_GRAY = (220, 220, 220)
BLUE = (100, 150, 255)

font = pygame.font.SysFont("Arial", 22)
small_font = pygame.font.SysFont("Arial", 18)

# İlk ürünler listesi (kategori bilgisi eklendi)
all_products = [
    {"name": "Elma", "price": 5, "category": "yiyecek"},
    {"name": "Erik", "price": 8, "category": "yiyecek"},
    {"name": "Süt", "price": 10, "category": "içecek"},
    {"name": "Peynir", "price": 15, "category": "yiyecek"},
    {"name": "Makarna", "price": 6, "category": "yiyecek"},
    {"name": "Mandalina", "price": 9, "category": "yiyecek"},
    {"name": "Portakal", "price": 7, "category": "yiyecek"},
    {"name": "Karpuz", "price": 12, "category": "yiyecek"},
    {"name": "Kiraz", "price": 20, "category": "yiyecek"},
    {"name": "Çilek", "price": 18, "category": "yiyecek"},
    {"name": "Banan", "price": 5, "category": "yiyecek"},
    {"name": "Kavun", "price": 14, "category": "yiyecek"},
    {"name": "Salatalık", "price": 4, "category": "yiyecek"},
    {"name": "Domates", "price": 3, "category": "yiyecek"},
    {"name": "Patates", "price": 6, "category": "yiyecek"},
    {"name": "Soğan", "price": 5, "category": "yiyecek"},
    {"name": "Marul", "price": 2, "category": "yiyecek"},
    {"name": "Havuç", "price": 3, "category": "yiyecek"},
    {"name": "Kabak", "price": 7, "category": "yiyecek"},
    {"name": "Limon", "price": 4, "category": "yiyecek"},
    {"name": "Zeytin", "price": 10, "category": "yiyecek"},
    {"name": "Elma Suyu", "price": 8, "category": "içecek"},
    {"name": "Portakal Suyu", "price": 9, "category": "içecek"},
    {"name": "İçecek", "price": 6, "category": "içecek"},
    {"name": "Su", "price": 2, "category": "içecek"},
    {"name": "Çikolata", "price": 5, "category": "yiyecek"},
    {"name": "Bisküvi", "price": 4, "category": "yiyecek"},
    {"name": "Cips", "price": 7, "category": "yiyecek"},
    {"name": "Reçel", "price": 10, "category": "yiyecek"},
    {"name": "Kek", "price": 8, "category": "yiyecek"},
    {"name": "Meyve Suyu", "price": 7, "category": "içecek"},
    {"name": "Kola", "price": 6, "category": "içecek"},
    {"name": "Limonata", "price": 4, "category": "içecek"},
    {"name": "Bira", "price": 10, "category": "içecek"},
    {"name": "Şarap", "price": 25, "category": "içecek"},
    {"name": "Soda", "price": 3, "category": "içecek"},
    {"name": "Peynirli Ekmek", "price": 12, "category": "yiyecek"},
    {"name": "Sandviç", "price": 8, "category": "yiyecek"},
    {"name": "Pizza", "price": 15, "category": "yiyecek"},
    {"name": "Köfte", "price": 20, "category": "yiyecek"},
    {"name": "Tavuk", "price": 18, "category": "yiyecek"},
    {"name": "Dana Et", "price": 25, "category": "yiyecek"},
    {"name": "Balık", "price": 18, "category": "yiyecek"},
    {"name": "Çorba", "price": 7, "category": "yiyecek"},
    {"name": "Meyve Salatası", "price": 12, "category": "yiyecek"},
    {"name": "Sebze Çorbası", "price": 8, "category": "yiyecek"},
    {"name": "Ekmek", "price": 3, "category": "yiyecek"},
    {"name": "Simit", "price": 2, "category": "yiyecek"},
    {"name": "Tuz", "price": 1, "category": "yiyecek"},
    {"name": "Şeker", "price": 2, "category": "yiyecek"},
    {"name": "Un", "price": 5, "category": "yiyecek"},
    {"name": "Pirinc", "price": 6, "category": "yiyecek"},
    {"name": "Makarnalık Un", "price": 7, "category": "yiyecek"},
    {"name": "Mısır Unu", "price": 6, "category": "yiyecek"},
    {"name": "Bulgur", "price": 5, "category": "yiyecek"},
    {"name": "Kuskus", "price": 7, "category": "yiyecek"},
    {"name": "Konserve Mısır", "price": 4, "category": "yiyecek"},
    {"name": "Konserve Domates", "price": 5, "category": "yiyecek"},
    {"name": "Yoğurt", "price": 6, "category": "yiyecek"},
    {"name": "Krema", "price": 10, "category": "yiyecek"},
    {"name": "Mayonez", "price": 5, "category": "yiyecek"},
    {"name": "Ketçap", "price": 4, "category": "yiyecek"},
    {"name": "Avokado", "price": 12, "category": "yiyecek"},
]

# Butonların konumları ve boyutları
food_button_rect = pygame.Rect(10, 50, 120, 30)
drink_button_rect = pygame.Rect(140, 50, 120, 30)
current_products = all_products  # Başlangıçta tüm ürünleri göster
cart = []
product_scroll_x = 0
cart_scroll = 0
animated_items = []  # {"product": ..., "y": ..., "target_y": ...}
cart_item_rects = [] # Sepetteki ürünlerin yazı alanlarının dikdörtgenleri

# Arama kutusu değişkenleri
search_rect = pygame.Rect(10, 10, 200, 30) # Arama kutusunun Y koordinatını güncelledik
search_text = ""
active_search = False

# Ürünleri ekrana çiz
def draw_product_list():
    global product_scroll_x, current_products

    product_area_y = 90  # Butonların altına kaydırıldı
    product_area_height = 150
    item_width = 140
    item_height = 50
    spacing = 20
    surface_width = len(current_products) * (item_width + spacing) + 20

    product_surface = pygame.Surface((surface_width, product_area_height))
    product_surface.fill(WHITE)

    x = 10
    y = 10
    for product in current_products:
        rect = pygame.Rect(x, y, item_width, item_height)
        pygame.draw.rect(product_surface, GRAY, rect)

        text = font.render(f"{product['name']}", True, BLACK)
        price = font.render(f"{product['price']}₺", True, BLACK)

        text_rect = text.get_rect(center=(rect.centerx, rect.centery - 8))
        price_rect = price.get_rect(center=(rect.centerx, rect.centery + 12))

        product_surface.blit(text, text_rect)
        product_surface.blit(price, price_rect)

        product['rect'] = pygame.Rect(rect.x - product_scroll_x, rect.y + product_area_y, rect.width, rect.height) # Y koordinatını güncelledik

        x += item_width + spacing

    max_scroll = max(0, surface_width - WIDTH)
    product_scroll_x = max(0, min(product_scroll_x, max_scroll))

    screen.blit(product_surface, (0, product_area_y), area=pygame.Rect(product_scroll_x, 0, WIDTH, product_area_height))

# Sepet bilgisini ekrana çiz
def draw_cart():
    global cart_scroll, cart_item_rects
    cart_area_y = 90 + 150 + 10 # Butonların ve ürün listesinin altına kaydırıldı
    cart_area_height = HEIGHT - cart_area_y - 50
    cart_surface_height = max(cart_area_height, len(cart) * 30 + 60)

    cart_surface = pygame.Surface((WIDTH, cart_surface_height))
    cart_surface.fill((230, 230, 230))

    cart_surface.blit(font.render("Sepetiniz:", True, BLACK), (30, 10))

    y = 40
    total = 0
    cart_item_rects = [] # Her çizimde dikdörtgenleri sıfırla
    for i, item in enumerate(cart):
        text_surface = font.render(f"{item['name']} x{item['quantity']} - {item['price'] * item['quantity']}₺", True, BLACK)
        text_rect = text_surface.get_rect(topleft=(40, y - cart_scroll)) # Kaydırmayı hesaba kat
        cart_surface.blit(text_surface, (40, y))
        cart_item_rects.append((text_rect, item['name'])) # Dikdörtgen ve ürün adını sakla
        y += 30
        total += item["price"] * item["quantity"]

    max_scroll = max(0, cart_surface_height - cart_area_height)
    cart_scroll = max(0, min(cart_scroll, max_scroll))

    screen.blit(cart_surface, (0, cart_area_y), area=pygame.Rect(0, cart_scroll, WIDTH, cart_area_height))

    kdv_orani = 0.20
    kdv_tutari = total * kdv_orani
    toplam_kdv_dahil = total + kdv_tutari

    pygame.draw.rect(screen, (200, 255, 200), (0, HEIGHT - 50, WIDTH, 50))
    toplam_text = font.render(f"Ara Toplam: {total:.2f}₺", True, BLACK)
    kdv_text = font.render(f"KDV (%20): {kdv_tutari:.2f}₺", True, BLACK)
    toplam_kdv_text = font.render(f"Toplam: {toplam_kdv_dahil:.2f}₺", True, GREEN)

    screen.blit(toplam_text, (10, HEIGHT - 45))
    screen.blit(kdv_text, (210, HEIGHT - 45))
    screen.blit(toplam_kdv_text, (410, HEIGHT - 45))

# Kategori butonlarını çiz
def draw_category_buttons():
    pygame.draw.rect(screen, BLUE, food_button_rect)
    food_text = font.render("Yiyecekler", True, WHITE)
    food_text_rect = food_text.get_rect(center=food_button_rect.center)
    screen.blit(food_text, food_text_rect)

    pygame.draw.rect(screen, GREEN, drink_button_rect)
    drink_text = font.render("İçecekler", True, WHITE)
    drink_text_rect = drink_text.get_rect(center=drink_button_rect.center)
    screen.blit(drink_text, drink_text_rect)

# Temizle butonunu çizer ve kontrol eder
def draw_clear_button():
    button_rect = pygame.Rect(WIDTH - 170, 10, 160, 30) # Y koordinatını arama kutusuyla aynı hizaya getirdik
    pygame.draw.rect(screen, RED, button_rect)
    text = font.render("Hepsini Temizle", True, WHITE)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
    return button_rect

# Arama kutusunu çiz
def draw_search_box():
    pygame.draw.rect(screen, LIGHT_GRAY, search_rect, 2)
    text_surface = font.render(search_text, True, BLACK)
    screen.blit(text_surface, (search_rect.x + 5, search_rect.y + 5))

# Sepet animasyonunu işler
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
        # Sepet içinde zaten varsa miktarı arttır
        found = False
        for item in cart:
            if item["name"] == anim["product"]["name"]:
                item["quantity"] += 1
                found = True
                break
        if not found:
            cart.append({"name": anim["product"]["name"], "price": anim["product"]["price"], "quantity": 1})

        animated_items.remove(anim)

# Mouse tıklama işlemleri
def check_click(pos):
    global active_search, current_products

    # Arama kutusuna tıklama
    if search_rect.collidepoint(pos):
        active_search = True
    else:
        active_search = False

    # Yiyecekler butonuna tıklama
    if food_button_rect.collidepoint(pos):
        current_products = [p for p in all_products if p['category'] == 'yiyecek']
        product_scroll_x = 0 # Kategori değişiminde kaydırmayı sıfırla
        return

    # İçecekler butonuna tıklama
    if drink_button_rect.collidepoint(pos):
        current_products = [p for p in all_products if p['category'] == 'içecek']
        product_scroll_x = 0 # Kategori değişiminde kaydırmayı sıfırla
        return

    # Hepsini Temizle butonuna tıklama
    if clear_button.collidepoint(pos):
        cart.clear()
        return

# Sepetteki bir ürüne tıklama (silme işlemi)
    cart_area_y = 90 + 150 + 10
    relative_y = pos[1] - cart_area_y + cart_scroll # Tıklamanın sepet içindeki göreli Y konumu
    for rect, product_name in cart_item_rects:
        if rect.collidepoint((pos[0], relative_y)):
            for item in cart:
                if item['name'] == product_name:
                    item['quantity'] -= 1
                    if item['quantity'] <= 0:
                        cart.remove(item)
                    return # Bir ürün silindikten sonra döngüden çık
            break # Ürün bulunamazsa döngüden çık

    # Sepete ekleme işlemi
    for product in current_products:
        if product.get('rect') and product['rect'].collidepoint(pos):
            animated_items.append({
                "product": product,
                "y": 130, # Ürün listesinin başlangıcı
                "target_y": cart_area_y + 10 # Sepet alanının başlangıcı
            })
            break

# Ana döngü
running = True
while running:
    screen.fill(WHITE)

    draw_search_box()
    draw_category_buttons()
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
                if event.pos[1] > 90 and event.pos[1] < 240: # Ürün listesi alanı
                    product_scroll_x -= 30
                elif event.pos[1] > 250 and event.pos[1] < HEIGHT - 50: # Sepet alanı
                    cart_scroll -= 20
            elif event.button == 5:
                if event.pos[1] > 90 and event.pos[1] < 240: # Ürün listesi alanı
                    product_scroll_x += 30
                elif event.pos[1] > 250 and event.pos[1] < HEIGHT - 50: # Sepet alanı
                    cart_scroll += 20

        elif event.type == pygame.KEYDOWN:
            if active_search:
                if event.key == pygame.K_RETURN:
                    # Arama yap
                    current_products = [p for p in all_products if search_text.lower() in p['name'].lower()]
                    product_scroll_x = 0 # Aramadan sonra kaydırmayı sıfırla
                elif event.key == pygame.K_BACKSPACE:
                    search_text = search_text[:-1]
                else:
                    search_text += event.unicode
            else:
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
