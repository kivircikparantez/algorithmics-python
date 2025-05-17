import pygame
import sys

pygame.init()

# Ekran ayarları
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alışveriş Sepeti")

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Font
font = pygame.font.SysFont(None, 36)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Sepet listesi
cart = []

# Görselleri yükle (GÖRSEL EKLE la, klasörde bunlar olacak)
elma_img = pygame.image.load("elma.png")
armut_img = pygame.image.load("armut.png")
cikolata_img = pygame.image.load("cikolata.png")
kola_img = pygame.image.load("kola.png")

# Görsel boyutlarını ayarla (80x80 yapak)
elma_img = pygame.transform.scale(elma_img, (80, 80))
armut_img = pygame.transform.scale(armut_img, (80, 80))
cikolata_img = pygame.transform.scale(cikolata_img, (80, 80))
kola_img = pygame.transform.scale(kola_img, (80, 80))

# Ürünler ve fiyatlar
urunler = [
    {"isim": "Elma", "resim": elma_img, "konum": (50, 50), "fiyat": 3},
    {"isim": "Armut", "resim": armut_img, "konum": (50, 150), "fiyat": 4},
    {"isim": "Çikolata", "resim": cikolata_img, "konum": (50, 250), "fiyat": 5},
    {"isim": "Kola", "resim": kola_img, "konum": (50, 350), "fiyat": 2},
]

# Kaydırma (scroll) özellikleri
scroll_y = 0
scroll_speed = 30  # Kaydırma hızı
scroll_max = 0  # En son kaydırma limiti
scrollable_height = 0  # Kaydırılabilir yükseklik
in_cart_screen = False  # Sepet ekranına geçiş kontrolü

def display_cart_screen():
    global scroll_y, scroll_max
    
    screen.fill(WHITE)

    total_price = sum(item["fiyat"] for item in cart)
    
    # Kaydırılabilir yükseklik
    scrollable_height = len(cart) * 40
    scroll_max = max(0, scrollable_height - (HEIGHT - 200))  # Eğer içerik ekranın yüksekliğinden büyükse kaydırma yapılabilir

    if scroll_y > scroll_max:
        scroll_y = scroll_max
    elif scroll_y < 0:
        scroll_y = 0
    
    y_offset = 100
    for i, item in enumerate(cart):
        item_text = f"{item['isim']} - {item['fiyat']} TL"
        text_surface = font.render(item_text, True, BLACK)
        screen.blit(text_surface, (50, y_offset + i * 40 - scroll_y))

        # Sepetten çıkarma butonu
        remove_button = pygame.Rect(600, y_offset + i * 40 - scroll_y, 150, 30)
        pygame.draw.rect(screen, RED, remove_button)
        remove_button_text = font.render("Çıkar", True, WHITE)
        screen.blit(remove_button_text, (remove_button.x + 10, remove_button.y + 5))

    # Toplam fiyat
    total_text = f"Toplam: {total_price} TL"
    total_surface = font.render(total_text, True, RED)
    screen.blit(total_surface, (50, y_offset + len(cart) * 40 - scroll_y + 20))

    # Ana menüye dönme butonu
    back_button = pygame.Rect(50, y_offset + len(cart) * 40 - scroll_y + 70, 200, 50)
    pygame.draw.rect(screen, GREEN, back_button)
    back_button_text = font.render("Ana Menü", True, WHITE)
    screen.blit(back_button_text, (back_button.x + 10, back_button.y + 10))

    # Kaydırma çubuğu
    if scroll_max > 0:
        scroll_bar_height = HEIGHT - 200  # Kaydırma çubuğunun yüksekliği
        scroll_bar_pos = (WIDTH - 20, 100 + (scroll_y / scroll_max) * (scroll_bar_height))  # Kaydırma çubuğu yeri
        pygame.draw.rect(screen, BLUE, pygame.Rect(scroll_bar_pos[0], scroll_bar_pos[1], 20, scroll_bar_height))

    pygame.display.flip()

def display_main_screen():
    screen.fill(WHITE)

    # Ürünleri çiz
    for urun in urunler:
        screen.blit(urun["resim"], urun["konum"])
    
    # Sepet yazısı
    sepet_yazisi = font.render(f"Sepet: {len(cart)} ürün", True, BLACK)
    screen.blit(sepet_yazisi, (200, 20))

    # Sepet butonu
    cart_button = pygame.Rect(600, 20, 150, 50)
    pygame.draw.rect(screen, GREEN, cart_button)
    cart_button_text = font.render("Sepeti Görüntüle", True, WHITE)
    screen.blit(cart_button_text, (cart_button.x + 10, cart_button.y + 10))
    
    pygame.display.flip()

# Ana döngü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            if in_cart_screen:  # Sepet ekranındaysak, ana menüye geri dön
                back_button = pygame.Rect(50, 200, 200, 50)
                if back_button.collidepoint(mx, my):
                    in_cart_screen = False

                # Sepetten ürün çıkarma
                for i, item in enumerate(cart):
                    remove_button = pygame.Rect(600, 100 + i * 40 - scroll_y, 150, 30)
                    if remove_button.collidepoint(mx, my):
                        cart.pop(i)
                        print(f"{item['isim']} sepetten çıkarıldı!")
                        break
            else:  # Ana ekrandaysak, ürünleri sepete ekle
                for urun in urunler:
                    x, y = urun["konum"]
                    if x <= mx <= x + 80 and y <= my <= y + 80:
                        cart.append(urun)  # Ürün sepete ekleniyor
                        print(f"{urun['isim']} sepete eklendi!")

                # Sepet butonuna tıklanmışsa, sepet ekranına geç
                cart_button = pygame.Rect(600, 20, 150, 50)
                if cart_button.collidepoint(mx, my):
                    in_cart_screen = True

        # Fare hareketi ile kaydırma
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[1] == 1:  # Orta fare tuşuna basılmışsa
                scroll_y += event.rel[1]  # Fare hareketi ile kaydırma
                if scroll_y > scroll_max:
                    scroll_y = scroll_max
                elif scroll_y < 0:
                    scroll_y = 0

    # Eğer sepet ekranında değilsek, ana ekranı göster
    if not in_cart_screen:
        display_main_screen()
    else:
        # Sepet ekranına geçildiğinde, sepet ekranını göster
        display_cart_screen()

    clock.tick(FPS)

pygame.quit()
