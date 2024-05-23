class Abonelik:
    def __init__(self, ad, soyad, email):
        self.ad = ad
        self.soyad = soyad
        self.email = email
        self.aktif = False
    
    def aboneligi_etkinlestir(self):
        self.aktif = True
    
    def aboneligi_pasiflestir(self):
        self.aktif = False

#chid classlarımız Abonelik ile alakalı
class AltAbonelik1(Abonelik):
    def __init__(self, ad, soyad, email):
        super().__init__(ad, soyad, email)
        self.paket = "Temel Paket"
        self.ucret = 50

class AltAbonelik2(Abonelik):
    def __init__(self, ad, soyad, email):
        super().__init__(ad, soyad, email)
        self.paket = "Orta Paket"
        self.ucret = 75

class AltAbonelik3(Abonelik):
    def __init__(self, ad, soyad, email):
        super().__init__(ad, soyad, email)
        self.paket = "Gelişmiş Paket"
        self.ucret = 100

class AltAbonelik4(Abonelik):
    def __init__(self, ad, soyad, email):
        super().__init__(ad, soyad, email)
        self.paket = "Premium Paket"
        self.ucret = 150

class AltAbonelik5(Abonelik):
    def __init__(self, ad, soyad, email):
        super().__init__(ad, soyad, email)
        self.paket = "Özel Paket"
        self.ucret = 200

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Örnek Kullanım  
#! 1kullanıcı sisteme girdikten sonra, sayfasında  mesela navbarda  abonelik adlı sayfaya ğeçsin 
#! orada bu işlemler olsun
abone1 = AltAbonelik1("Ahmet", "Yılmaz", "ahmet@example.com")
abone1.aboneligi_etkinlestir()
print(f"{abone1.ad} {abone1.soyad}'in {abone1.paket} aboneliği {abone1.aktif} ve fiyatı {abone1.ucret}")



#aboneliğe göre avantajlar olsun AltAbonelik5 sunu yapıyor AltAbonelik1 yapamıyor gibisinden

