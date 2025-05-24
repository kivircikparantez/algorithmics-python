import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 650  # Pencere boyutunu biraz büyüttük
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gelişmiş Alışveriş Sepeti App")

clock = pygame.time.Clock()

# Renkler
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)
RED = (200, 50, 50)
LIGHT_GRAY = (220, 220, 220)
BLUE = (100, 150, 255)
PURPLE = (150, 50, 200)
ORANGE = (255, 165, 0)
DARK_GREEN = (0, 100, 0)

font = pygame.font.SysFont("Arial", 22)
small_font = pygame.font.SysFont("Arial", 18)

# Ürün veritabanını güncelledik (daha fazla kategori ekledik)
all_products = [
    {"name": "Elma", "price": 5, "category": "Meyve"},
    {"name": "Erik", "price": 8, "category": "Meyve"},
    {"name": "Süt", "price": 10, "category": "Süt Ürünleri"},
    {"name": "Peynir", "price": 15, "category": "Süt Ürünleri"},
    {"name": "Makarna", "price": 6, "category": "Temel Gıda"},
    {"name": "Mandalina", "price": 9, "category": "Meyve"},
    {"name": "Portakal", "price": 7, "category": "Meyve"},
    {"name": "Karpuz", "price": 12, "category": "Meyve"},
    {"name": "Kiraz", "price": 20, "category": "Meyve"},
    {"name": "Çilek", "price": 18, "category": "Meyve"},
    {"name": "Banan", "price": 5, "category": "Meyve"},
    {"name": "Kavun", "price": 14, "category": "Meyve"},
    {"name": "Salatalık", "price": 4, "category": "Sebze"},
    {"name": "Domates", "price": 3, "category": "Sebze"},
    {"name": "Patates", "price": 6, "category": "Sebze"},
    {"name": "Soğan", "price": 5, "category": "Sebze"},
    {"name": "Marul", "price": 2, "category": "Sebze"},
    {"name": "Havuç", "price": 3, "category": "Sebze"},
    {"name": "Kabak", "price": 7, "category": "Sebze"},
    {"name": "Limon", "price": 4, "category": "Meyve"},
    {"name": "Zeytin", "price": 10, "category": "Kahvaltılık"},
    {"name": "Elma Suyu", "price": 8, "category": "İçecek"},
    {"name": "Portakal Suyu", "price": 9, "category": "İçecek"},
    {"name": "Meyve Suyu", "price": 7, "category": "İçecek"},
    {"name": "Su", "price": 2, "category": "İçecek"},
    {"name": "Çikolata", "price": 5, "category": "Atıştırmalık"},
    {"name": "Bisküvi", "price": 4, "category": "Atıştırmalık"},
    {"name": "Cips", "price": 7, "category": "Atıştırmalık"},
    {"name": "Reçel", "price": 10, "category": "Kahvaltılık"},
    {"name": "Kek", "price": 8, "category": "Atıştırmalık"},
    {"name": "Kola", "price": 6, "category": "İçecek"},
    {"name": "Limonata", "price": 4, "category": "İçecek"},
    {"name": "Soda", "price": 3, "category": "İçecek"},
    {"name": "Peynirli Ekmek", "price": 12, "category": "Hazır Gıda"},
    {"name": "Sandviç", "price": 8, "category": "Hazır Gıda"},
    {"name": "Pizza", "price": 15, "category": "Hazır Gıda"},
    {"name": "Ekmek", "price": 3, "category": "Fırın Ürünleri"},
    {"name": "Simit", "price": 2, "category": "Fırın Ürünleri"},
    {"name": "Tuz", "price": 1, "category": "Baharat"},
    {"name": "Şeker", "price": 2, "category": "Temel Gıda"},
    {"name": "Un", "price": 5, "category": "Temel Gıda"},
    {"name": "Pirinc", "price": 6, "category": "Temel Gıda"},
    {"name": "Bulgur", "price": 5, "category": "Temel Gıda"},
    {"name": "Yoğurt", "price": 6, "category": "Süt Ürünleri"},
    {"name": "Mayonez", "price": 5, "category": "Sos"},
    {"name": "Ketçap", "price": 4, "category": "Sos"},
    {"name": "Çamaşır Suyu", "price": 8, "category": "Temizlik"},
    {"name": "Deterjan", "price": 12, "category": "Temizlik"},
    {"name": "Şampuan", "price": 15, "category": "Kişisel Bakım"},
    {"name": "Diş Macunu", "price": 10, "category": "Kişisel Bakım"}
]

# Tüm kategorileri otomatik olarak çıkarıyoruz
all_categories = sorted(list(set(product["category"] for product in all_products)))
current_category = "Tüm Ürünler"  # Varsayılan kategori

# Butonların konumları ve boyutları
category_buttons = []
button_width = 100
button_height = 30
buttons_per_row = 7  # Her satıra 5 buton
button_spacing = 1

# Kategori butonlarını oluştur
for i, category in enumerate(["Tüm Ürünler"] + all_categories):
    row = i // buttons_per_row
    col = i % buttons_per_row
    x = 10 + col * (button_width + button_spacing)
    y = 50 + row * (button_height + button_spacing)
    category_buttons.append({
        "rect": pygame.Rect(x, y, button_width, button_height),
        "category": category,
        "color": BLUE if category == "Tüm Ürünler" else GRAY
    })

current_products = all_products  # Başlangıçta tüm ürünleri göster
cart = []
product_scroll_x = 0
cart_scroll = 0
animated_items = []
cart_item_rects = []

# Arama kutusu
search_rect = pygame.Rect(10, 10, 300, 30)
search_text = ""
active_search = False

# Ürünleri ekrana çiz
def draw_product_list():
    global product_scroll_x, current_products

    product_area_y = 120  # Kategori butonlarının altına kaydırdık
    product_area_height = 180  # Ürün listesi alanını biraz büyüttük
    item_width = 160  # Ürün kartlarını biraz genişlettik
    item_height = 60   # Ürün kartlarını biraz yüksek yaptık
    spacing = 15
    surface_width = len(current_products) * (item_width + spacing) + 20

    product_surface = pygame.Surface((surface_width, product_area_height))
    product_surface.fill(WHITE)

    x = 10
    y = 10
    for product in current_products:
        rect = pygame.Rect(x, y, item_width, item_height)
        pygame.draw.rect(product_surface, GRAY, rect, border_radius=5)  # Köşeleri yuvarlak yaptık
        
        # Ürün adı (kısaltılmış)
        name = product['name'] if len(product['name']) < 15 else product['name'][:12] + "..."
        text = small_font.render(name, True, BLACK)
        
        # Fiyat
        price = font.render(f"{product['price']}₺", True, BLACK)
        
        # Kategori (küçük yazı)
        category = small_font.render(product['category'], True, (100, 100, 100))

        product_surface.blit(text, (rect.x + 10, rect.y + 5))
        product_surface.blit(price, (rect.x + 10, rect.y + 30))
        product_surface.blit(category, (rect.x + 10, rect.y + 50))

        product['rect'] = pygame.Rect(rect.x - product_scroll_x, rect.y + product_area_y, rect.width, rect.height)

        x += item_width + spacing

    max_scroll = max(0, surface_width - WIDTH)
    product_scroll_x = max(0, min(product_scroll_x, max_scroll))

    screen.blit(product_surface, (0, product_area_y), area=pygame.Rect(product_scroll_x, 0, WIDTH, product_area_height))

# Sepet bilgisini ekrana çiz
def draw_cart():
    global cart_scroll, cart_item_rects
    cart_area_y = 120 + 180 + 10
    cart_area_height = HEIGHT - cart_area_y - 60  # Alt boşluk biraz daha fazla
    cart_surface_height = max(cart_area_height, len(cart) * 40 + 60)  # Satır aralığını artırdık

    cart_surface = pygame.Surface((WIDTH - 20, cart_surface_height))
    cart_surface.fill((240, 240, 240))
    pygame.draw.rect(cart_surface, (200, 200, 200), (0, 0, WIDTH-20, cart_surface_height), 2, border_radius=5)

    title = font.render("SEPETİNİZ", True, BLACK)
    cart_surface.blit(title, (20, 15))

    y = 50
    total = 0
    cart_item_rects = []
    for i, item in enumerate(cart):
        # Arkaplan rengi (zebra deseni)
        bg_color = (230, 230, 230) if i % 2 == 0 else (220, 220, 220)
        pygame.draw.rect(cart_surface, bg_color, (10, y-5, WIDTH-40, 35))
        
        # Ürün bilgisi
        text = f"{item['name']} x{item['quantity']} = {item['price'] * item['quantity']}₺"
        text_surface = font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(topleft=(20, y - cart_scroll))
        cart_surface.blit(text_surface, (20, y))
        
        # Silme butonu
        delete_rect = pygame.Rect(WIDTH - 80, y, 60, 25)
        pygame.draw.rect(cart_surface, RED, delete_rect, border_radius=3)
        delete_text = small_font.render("Sil", True, WHITE)
        cart_surface.blit(delete_text, (WIDTH - 70, y+3))
        
        cart_item_rects.append((text_rect, delete_rect, item['name']))
        y += 40
        total += item["price"] * item["quantity"]

    max_scroll = max(0, cart_surface_height - cart_area_height)
    cart_scroll = max(0, min(cart_scroll, max_scroll))

    screen.blit(cart_surface, (10, cart_area_y), area=pygame.Rect(0, cart_scroll, WIDTH, cart_area_height))

    # Toplam bilgisi
    pygame.draw.rect(screen, (200, 230, 200), (0, HEIGHT - 60, WIDTH, 60), border_radius=5)
    pygame.draw.rect(screen, (0, 150, 0), (0, HEIGHT - 60, WIDTH, 60), 2, border_radius=5)
    
    kdv_orani = 0.20
    kdv_tutari = total * kdv_orani
    toplam_kdv_dahil = total + kdv_tutari

    toplam_text = font.render(f"Ara Toplam: {total:.2f}₺", True, DARK_GREEN)
    kdv_text = font.render(f"KDV (%20): {kdv_tutari:.2f}₺", True, DARK_GREEN)
    toplam_kdv_text = font.render(f"GENEL TOPLAM: {toplam_kdv_dahil:.2f}₺", True, BLACK)

    screen.blit(toplam_text, (20, HEIGHT - 50))
    screen.blit(kdv_text, (250, HEIGHT - 50))
    screen.blit(toplam_kdv_text, (500, HEIGHT - 50))

# Kategori butonlarını çiz
def draw_category_buttons():
    for button in category_buttons:
        pygame.draw.rect(screen, button["color"], button["rect"], border_radius=5)
        pygame.draw.rect(screen, BLACK, button["rect"], 2, border_radius=5)  # Kenarlık
        
        # Buton metni (kategori adı)
        text = small_font.render(button["category"], True, BLACK)
        text_rect = text.get_rect(center=button["rect"].center)
        screen.blit(text, text_rect)

# Arama kutusunu çiz
def draw_search_box():
    color = BLUE if active_search else BLACK
    pygame.draw.rect(screen, WHITE, search_rect, border_radius=5)
    pygame.draw.rect(screen, color, search_rect, 2, border_radius=5)
    
    text = search_text
    if active_search and not text:
        hint = small_font.render("Ürün ara...", True, (150, 150, 150))
        screen.blit(hint, (search_rect.x + 10, search_rect.y + 8))
    elif text:
        text_surface = font.render(text, True, BLACK)
        screen.blit(text_surface, (search_rect.x + 10, search_rect.y + 8))

# Temizle butonunu çiz
def draw_clear_button():
    button_rect = pygame.Rect(WIDTH - 120, 10, 110, 30)
    pygame.draw.rect(screen, RED, button_rect, border_radius=5)
    pygame.draw.rect(screen, BLACK, button_rect, 2, border_radius=5)
    text = small_font.render("Sepeti Temizle", True, WHITE)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
    return button_rect

# Sepet animasyonunu işler
def handle_animations():
    finished = []
    for anim in animated_items:
        anim["y"] += 10
        product = anim["product"]
        rect = pygame.Rect(200, anim["y"], 160, 60)
        pygame.draw.rect(screen, GRAY, rect, border_radius=5)
        text = font.render(product["name"], True, BLACK)
        price = font.render(f"{product['price']}₺", True, BLACK)
        screen.blit(text, (rect.x + 10, rect.y + 5))
        screen.blit(price, (rect.x + 10, rect.y + 30))
        if anim["y"] >= anim["target_y"]:
            finished.append(anim)

    for anim in finished:
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
    global active_search, current_products, current_category

    # Arama kutusuna tıklama
    if search_rect.collidepoint(pos):
        active_search = True
        return

    active_search = False

    # Kategori butonlarına tıklama
    for button in category_buttons:
        if button["rect"].collidepoint(pos):
            current_category = button["category"]
            # Tüm butonların rengini sıfırla
            for btn in category_buttons:
                btn["color"] = GRAY
            # Seçili butonun rengini değiştir
            button["color"] = BLUE
            
            if current_category == "Tüm Ürünler":
                current_products = all_products
            else:
                current_products = [p for p in all_products if p['category'] == current_category]
            
            # Arama metni varsa, filtrelemeyi koru
            if search_text:
                current_products = [p for p in current_products if search_text.lower() in p['name'].lower()]
            
            product_scroll_x = 0
            return

    # Hepsini Temizle butonuna tıklama
    if clear_button.collidepoint(pos):
        cart.clear()
        return

    # Sepetteki silme butonlarına tıklama
    cart_area_y = 310
    relative_y = pos[1] - cart_area_y + cart_scroll
    for text_rect, delete_rect, product_name in cart_item_rects:
        if delete_rect.collidepoint((pos[0]-10, relative_y)):  # -10 çünkü sepet 10px içeriden başlıyor
            for item in cart:
                if item['name'] == product_name:
                    cart.remove(item)
                    return

    # Sepete ekleme işlemi
    for product in current_products:
        if product.get('rect') and product['rect'].collidepoint(pos):
            animated_items.append({
                "product": product,
                "y": 150,
                "target_y": cart_area_y + 10
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
            elif event.button == 4:  # Fare tekerleği yukarı
                if 120 < event.pos[1] < 300:  # Ürün listesi alanı
                    product_scroll_x = max(0, product_scroll_x - 30)
                elif 310 < event.pos[1] < HEIGHT - 60:  # Sepet alanı
                    cart_scroll = max(0, cart_scroll - 20)
            elif event.button == 5:  # Fare tekerleği aşağı
                if 120 < event.pos[1] < 300:  # Ürün listesi alanı
                    max_scroll = max(0, len(current_products) * 175 - WIDTH)
                    product_scroll_x = min(max_scroll, product_scroll_x + 30)
                elif 310 < event.pos[1] < HEIGHT - 60:  # Sepet alanı
                    max_scroll = max(0, len(cart) * 40 + 60 - (HEIGHT - 310 - 60))
                    cart_scroll = min(max_scroll, cart_scroll + 20)

        elif event.type == pygame.KEYDOWN:
            if active_search:
                if event.key == pygame.K_RETURN:
                    # Arama yap
                    search_term = search_text.lower()
                    if current_category == "Tüm Ürünler":
                        current_products = [p for p in all_products if search_term in p['name'].lower()]
                    else:
                        current_products = [p for p in all_products if p['category'] == current_category and search_term in p['name'].lower()]
                    product_scroll_x = 0
                elif event.key == pygame.K_BACKSPACE:
                    search_text = search_text[:-1]
                    # Arama metni değiştiğinde filtrelemeyi güncelle
                    search_term = search_text.lower()
                    if current_category == "Tüm Ürünler":
                        current_products = [p for p in all_products if search_term in p['name'].lower()]
                    else:
                        current_products = [p for p in all_products if p['category'] == current_category and search_term in p['name'].lower()]
                    product_scroll_x = 0
                else:
                    search_text += event.unicode
            else:
                if event.key == pygame.K_LEFT:
                    product_scroll_x = max(0, product_scroll_x - 30)
                elif event.key == pygame.K_RIGHT:
                    max_scroll = max(0, len(current_products) * 175 - WIDTH)
                    product_scroll_x = min(max_scroll, product_scroll_x + 30)
                elif event.key == pygame.K_UP:
                    cart_scroll = max(0, cart_scroll - 20)
                elif event.key == pygame.K_DOWN:
                    max_scroll = max(0, len(cart) * 40 + 60 - (HEIGHT - 310 - 60))
                    cart_scroll = min(max_scroll, cart_scroll + 20)

    pygame.display.flip()
    clock.tick(60)
