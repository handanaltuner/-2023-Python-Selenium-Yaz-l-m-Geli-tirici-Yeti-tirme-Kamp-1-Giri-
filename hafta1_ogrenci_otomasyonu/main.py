#Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

#Bu öğrenci kayıt sistemine;

#Aldığı isim soy isim ile listeye öğrenci ekleyen
#Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
#Listeye birden fazla öğrenci eklemeyi mümkün kılan
#Listedeki tüm öğrencileri tek tek ekrana yazdıran
#Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
#Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
#fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

#Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.



ogrencilerListesi = []

def ogrenciEkle():
    print("Öğrenci ekleme işlemleri")
    adSoyad=input("Ad Soyad Giriniz: ")
    ogrencilerListesi.append(adSoyad)
    ogrencilerListesi.index(adSoyad)
    print("Kayıt Başarı ile eklendi" )
    print(ogrencilerListesi)

def ogrenciSil():
    adSoyad=input("Lütfen silinecek olan Ad ve Soyadı giriniz: ")
    for ogrenci in ogrencilerListesi:
        if ogrenci==adSoyad:
            ogrencilerListesi.remove(adSoyad)
    print("Öğrenci Silindi")

def cokluOgrenciEkleme():
    ogrenciEkle=int(input("Eklemek istediğiniz öğrenci ad ve soyadını giriniz: "))
    for i in range(ogrenciEkle):
        ogrenciEkle(input("Eklemek istediğiniz öğrenci adını giriniz"))
        ogrenciler.append(cokluEkle)
    cokluOgrenciEkleme()
    print("Birden fazla öğrenci listeye eklendi")

def ogrencileriListeleme():
    for ogrenciler in range(len(ogrencilerListesi)): #ogrenciler dongusunde ne kadar dongu varsa o kadar donecek
        print("{adSoyad[ogrenciler]}")
    print("Öğrenciler listendi ve ekrana yazdırıldı")

def cokluOgrenciSilme():
        ogrenciSilinecekSayisi = int(input("Kaç kişi sileceksiniz: "))
        ogrenciSilinecekListesi = []
        x = 0
        while ogrenciSilinecekSayisi:
         x +=1
        OgrenciSilinmesi = input(
            "Silinecek değerleri isim ve soyisim olarak giriniz: ")
        ogrenciSilinecekListesi.append(OgrenciSilinmesi)

        for i in ogrencilerListesi:
            if i in ogrenciSilinecekListesi:
                ogrencilerListesi.remove(i)
            else:
                continue
            if ogrenciSilinecekSayisi==x:
                break
        print(ogrenciSilinecekListesi)
        print("Birden fazla öğrenci listeden silindi")


def menu():
    print("\n"*2)
    fonksiyonListesi=(ogrenciEkle,ogrenciSil,cokluOgrenciEkleme,ogrencilerListesi,cokluOgrenciSilme)
    while True:
        print("1-Öğrenci İsim Soyisim ekle")
        print("2-Öğrenci İsim Soyisim ile eşleşen değeri kaldır")
        print("3-Birden fazla öğrenci ekleyin")
        print("4-Listedeki tüm öğrencileri ekrana yazdır")
        print("5-Listdeki birden fazla öğrenciyi silin")
        print("0-Programdan çık")
        seciminiz=int(input("Lütfen yapmak istediğiniz işlemi seçiniz (0-5): "))
        print("\n"*40) #boşluk bırakma
        if seciminiz<=5 and seciminiz>=1:
            fonksiyonListesi[seciminiz-1]() #1Girdiğimde ilk değeri istiyorsak seçiminiz 1 azaltılacak, o yüzden -1 yaziyoruz. Bunlar da birer fonksiyon olduğu için () yaparız.
            print("Geçerli işlem seçildi")
            print("\n" * 2)
        elif seciminiz==0:
             print("Çıkış yapılıyor")
             break
        else:
            print("Lütfen seçim için 0 ile 5 arası bir rakam giriniz")
            
menu()



