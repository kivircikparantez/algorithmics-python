import pygame
import sys
import random

# Pygame başlatma
pygame.init()

# Ekran ayarları
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alışveriş Sepeti Uygulaması")

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (240, 240, 240)
BLUE = (0, 120, 215)
GREEN = (0, 150, 0)
RED = (200, 0, 0)

# Fontlar
font_small = pygame.font.SysFont('Arial', 14)
font_medium = pygame.font.SysFont('Arial', 18)
font_large = pygame.font.SysFont('Arial', 24)

# Ürün verileri
products = [
    {"id": 1, "name": "Bilgisayar", "price": 12000, "image": None},
    {"id": 2, "name": "Telefon", "price": 8000, "image": None},
    {"id": 3, "name": "Tablet", "price": 5000, "image": None},
    {"id": 4, "name": "Kulaklık", "price": 500, "image": None},
    {"id": 5, "name": "Klavye", "price": 400, "image": None},
    {"id": 6, "name": "Fare", "price": 300, "image": None},
    {"id": 7, "name": "Monitör", "price": 3500, "image": None},
    {"id": 8, "name": "Hoparlör", "price": 600, "image": None},
    {"id": 9, "name": "Webcam", "price": 450, "image": None},
    {"id": 10, "name": "Mikrofon", "price": 550, "image": None},
    {"id": 11, "name": "SSD", "price": 1200, "image": None},
    {"id": 12, "name": "RAM", "price": 800, "image": None},
]

# Ürünler için rastgele renkler oluştur
for product in products:
    product["color"] = (random.randint(100, 200), random.randint(100, 200), random.randint(100, 200))

# Sepet
cart = []
cart_scroll_position = 0
product_scroll_position = 0
animation_in_progress = False
animation_product = None
animation_start_pos = (0, 0)
animation_progress = 0

def draw_product_card(product, x, y, width, height):
    # Dikdörtgen çiz
    pygame.draw.rect(screen, product["color"], (x, y, width, height))
    
    # Ürün adı
    name_text = font_medium.render(product["name"], True, BLACK)
    screen.blit(name_text, (x + 10, y + 10))
    
    # Ürün fiyatı
    price_text = font_medium.render(f"{product['price']} TL", True, BLACK)
    screen.blit(price_text, (x + 10, y + height - 30))
    
    # Sepete ekle butonu
    pygame.draw.rect(screen, GREEN, (x + width - 100, y + height - 30, 90, 25))
    add_text = font_small.render("Sepete Ekle", True, WHITE)
    screen.blit(add_text, (x + width - 95, y + height - 25))

def draw_products():
    # Ürünlerin bulunduğu alan
    product_area_width = WIDTH - 300
    product_area_height = HEIGHT
    
    # Ürünleri çiz
    visible_products = 6  # Ekranda görünecek maksimum ürün sayısı
    start_index = int(product_scroll_position / 180)
    
    for i in range(start_index, min(start_index + visible_products, len(products))):
        product = products[i]
        row = (i - start_index) // 2
        col = (i - start_index) % 2
        product_y = 20 + row * 180 - (product_scroll_position % 180)
        draw_product_card(product, 20 + col * 240, product_y, 220, 160)
    
    # Scroll çubuğu (eğer gerekliyse)
    if len(products) > visible_products:
        total_height = (len(products) + 1) // 2 * 180
        visible_height = visible_products // 2 * 180
        scrollbar_height = visible_height * (visible_height / total_height)
        scrollbar_y = (product_scroll_position / total_height) * visible_height
        
        pygame.draw.rect(screen, GRAY, (WIDTH - 320, scrollbar_y, 5, scrollbar_height))

def draw_cart():
    # Sepet arkaplanı
    pygame.draw.rect(screen, LIGHT_GRAY, (WIDTH - 300, 0, 300, HEIGHT))
    
    # Sepet başlığı
    pygame.draw.rect(screen, BLUE, (WIDTH - 300, 0, 300, 40))
    cart_title = font_large.render("Sepet", True, WHITE)
    screen.blit(cart_title, (WIDTH - 250, 10))
    
    # Sepet içeriği
    content_y = 50
    max_content_height = HEIGHT - 200
    content_height = len(cart) * 60
    
    # Scroll için klip alanı oluştur
    clip_rect = pygame.Rect(WIDTH - 300, 50, 300, max_content_height)
    screen.set_clip(clip_rect)
    
    # Sepet öğelerini çiz
    for i, item in enumerate(cart):
        item_y = 50 + i * 60 - cart_scroll_position
        
        # Sepet öğesi kutusu
        pygame.draw.rect(screen, WHITE, (WIDTH - 290, item_y, 280, 50))
        
        # Ürün bilgileri
        name_text = font_medium.render(item["name"], True, BLACK)
        screen.blit(name_text, (WIDTH - 280, item_y + 5))
        
        price_text = font_small.render(f"{item['price']} TL", True, BLACK)
        screen.blit(price_text, (WIDTH - 280, item_y + 25))
        
        # Çıkarma butonu
        pygame.draw.rect(screen, RED, (WIDTH - 80, item_y + 10, 70, 30))
        remove_text = font_small.render("Çıkar", True, WHITE)
        screen.blit(remove_text, (WIDTH - 75, item_y + 18))
    
    # Klipi sıfırla
    screen.set_clip(None)
    
    # Scroll çubuğu (eğer içerik yüksekliği maksimumu aşıyorsa)
    if content_height > max_content_height:
        scrollbar_height = max_content_height * (max_content_height / content_height)
        scrollbar_y = 50 + (cart_scroll_position / content_height) * max_content_height
        
        pygame.draw.rect(screen, GRAY, (WIDTH - 10, scrollbar_y, 5, scrollbar_height))
    
    # Toplam alanı
    pygame.draw.rect(screen, WHITE, (WIDTH - 300, HEIGHT - 150, 300, 150))
    
    # Ara toplam
    subtotal = sum(item["price"] for item in cart)
    subtotal_text = font_medium.render(f"Ara Toplam: {subtotal} TL", True, BLACK)
    screen.blit(subtotal_text, (WIDTH - 280, HEIGHT - 140))
    
    # KDV (%18)
    kdv = subtotal * 0.18
    kdv_text = font_medium.render(f"KDV (%18): {kdv:.2f} TL", True, BLACK)
    screen.blit(kdv_text, (WIDTH - 280, HEIGHT - 110))
    
    # Toplam
    total = subtotal + kdv
    total_text = font_large.render(f"Toplam: {total:.2f} TL", True, BLACK)
    screen.blit(total_text, (WIDTH - 280, HEIGHT - 80))
    
    # Satın al butonu
    pygame.draw.rect(screen, GREEN, (WIDTH - 150, HEIGHT - 40, 130, 30))
    buy_text = font_medium.render("Satın Al", True, WHITE)
    screen.blit(buy_text, (WIDTH - 120, HEIGHT - 35))

def animate_product_to_cart(product, start_pos):
    global animation_in_progress, animation_product, animation_start_pos, animation_progress
    
    animation_in_progress = True
    animation_product = product
    animation_start_pos = start_pos
    animation_progress = 0

def update_animation():
    global animation_in_progress, animation_progress
    
    if animation_in_progress:
        animation_progress += 0.02
        if animation_progress >= 1:
            cart.append(animation_product)
            animation_in_progress = False

def draw_animation():
    if animation_in_progress:
        start_x, start_y = animation_start_pos
        end_x = WIDTH - 150
        end_y = HEIGHT - 150
        
        # Bezier eğrisi için kontrol noktaları
        control_x = (start_x + end_x) // 2
        control_y = start_y - 100
        
        # Animasyon ilerlemesine göre konum hesapla
        t = animation_progress
        x = (1-t)**2 * start_x + 2*(1-t)*t*control_x + t**2*end_x
        y = (1-t)**2 * start_y + 2*(1-t)*t*control_y + t**2*end_y
        
        # Ürün simgesini çiz
        pygame.draw.circle(screen, animation_product["color"], (int(x), int(y)), 15)
        product_initial = animation_product["name"][0]
        initial_text = font_small.render(product_initial, True, WHITE)
        screen.blit(initial_text, (int(x)-5, int(y)-7))

def handle_mouse_click(pos):
    global cart_scroll_position, product_scroll_position
    
    mouse_x, mouse_y = pos
    
    # Ürün alanı scroll kontrolü
    if mouse_x < WIDTH - 300:
        # Sepete ekleme butonları
        visible_products = 6
        start_index = int(product_scroll_position / 180)
        
        for i in range(start_index, min(start_index + visible_products, len(products))):
            product = products[i]
            row = (i - start_index) // 2
            col = (i - start_index) % 2
            product_y = 20 + row * 180 - (product_scroll_position % 180)
            
            # Sepete ekle butonuna tıklama kontrolü
            if (20 + col * 240 + 220 - 100 <= mouse_x <= 20 + col * 240 + 220 - 10 and 
                product_y + 160 - 30 <= mouse_y <= product_y + 160 - 5):
                animate_product_to_cart(product.copy(), (20 + col * 240 + 110, product_y + 80))
                return
    
    # Sepetten çıkarma butonları
    elif WIDTH - 300 <= mouse_x <= WIDTH:
        for i, item in enumerate(cart):
            item_y = 50 + i * 60 - cart_scroll_position
            
            # Çıkarma butonuna tıklama kontrolü
            if (WIDTH - 80 <= mouse_x <= WIDTH - 10 and 
                item_y + 10 <= mouse_y <= item_y + 40 and
                50 <= mouse_y <= 50 + (HEIGHT - 200)):
                cart.pop(i)
                return

# Ana döngü
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Sol tıklama
                handle_mouse_click(event.pos)
        
        elif event.type == pygame.MOUSEWHEEL:
            # Scroll işlemi
            if pygame.mouse.get_pos()[0] < WIDTH - 300:  # Ürün alanında
                max_product_scroll = max(0, ((len(products) + 1) // 2) * 180 - (HEIGHT - 20))
                product_scroll_position = max(0, min(product_scroll_position - event.y * 20, max_product_scroll))
            else:  # Sepet alanında
                max_cart_scroll = max(0, len(cart) * 60 - (HEIGHT - 200))
                cart_scroll_position = max(0, min(cart_scroll_position - event.y * 20, max_cart_scroll))
    
    # Ekranı temizle
    screen.fill(WHITE)
    
    # Ürünleri çiz
    draw_products()
    
    # Sepeti çiz
    draw_cart()
    
    # Animasyonu güncelle ve çiz
    update_animation()
    draw_animation()
    
    # Ekranı güncelle
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
