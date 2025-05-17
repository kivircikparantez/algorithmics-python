#İMPORT BÖLÜMÜ
import pygame
#EKRAN OLUŞTURMA
ekran = pygame.display.set_mode((800, 600))
#ÜRÜNLERİN LİSTESİ
urunler = [{urun:"Çilek", fiyat :50},{urun:"Elma", fiyat: 25},{urun:"Muz",fiyat:75}]
#ÜRÜNLERİN KUTULARI VE YAZILARI

elma_resmi = pygame.image.load("elma.png")
elma_kutu= pygame.Rect(-200,150,elma_resmi.get_width(),elma_resmi.get_height())

muz_resmi = pygame.image.load("muz.png")
muz_kutu= pygame.Rect(-50,150,muz_resmi.get_width(),muz_resmi.get_height())

çilek_resmi = pygame.image.load("çilek.png")
çilek_kutu = pygame.Rect(200,150,çilek_resmi.get_width(),çilek_resmi.get_height())

#TIKLAMA ALGILAMA VE ÜRÜN ANİMASYONU

def elma_kutusu_tiklandi():
    if pygame.when_clicked.elma_kutu == collide_point(mouse_x,mouse_y)
    
GPT PROMPT =merhaba reis ben başlangıç seviyesi python bilgisine sahibim ve bir proje oluşturmak istiyorum. 
Oluşturacağım proje aslında alışveriş sepeti gibi . harika değilmi . 
öncelikle elma ,muz ve çilek meyvelerinin isminin yazılı olduğu 3 kutu olacak bu kutulardan  
birine tıklandığında o kutu hareket ederek alttaki "sepetim" kısmına eklenecek ve eklenen toplam ürünlerin 
fiyatı gözükecek (%18 KDV uygalanacak) ayrıca sepet içeriği ekrana sığmazsa örneğin 100 adet elma alırsam ekrana 
sığmayacağı için mousenin scroll tuşu ile sepette yukarı aşağı kaydırma özelliği olması gerekiyor. bana neyi neden
yapmam gerektiğini tane tane anlatarak bir yol haritası oluştur
