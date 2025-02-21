print("╔════════════════════════╗")
print("║       OYUNLAR          ║")
print("║1-KAPLUMBAĞA YARIŞI     ║")
print("║2-ADAM ASMACA           ║")
print("║3-TAŞ-KAĞIT-MAKAS       ║")
print("║    Seçimini Yap        ║")
print("╚════════════════════════╝")

s=input("Seçiminizi Yapınız:")

if s == "1":

    import turtle
    import random

    t = turtle.Turtle()
    t.up()
    t.goto(-100, 100)
    t.down()
    t.speed(0)

    # yarış pisti
    for i in range(15):
        t.write(i)
        t.right(90)
        t.forward(200)
        t.left(180)
        t.forward(200)
        t.right(90)
        t.forward(20)

    # kablumbağaları oluşturma
    birinci = turtle.Turtle()
    birinci.shape("turtle")
    birinci.color("red")
    birinci.up()
    birinci.goto(-120, 70)
    birinci.down()

    ikinci = turtle.Turtle()
    ikinci.shape("turtle")
    ikinci.color("blue")
    ikinci.up()
    ikinci.goto(-120, 40)
    ikinci.down()

    ucuncu = turtle.Turtle()
    ucuncu.shape("turtle")
    ucuncu.color("yellow")
    ucuncu.up()
    ucuncu.goto(-120, 10)
    ucuncu.down()

    # taraftarlar
    x = random.randint(1, 10)
    for i in range(x):
        taraftar = turtle.Turtle()
        k = random.randint(0, 255) / 255.0  # Renk değerlerini normalize et
        y = random.randint(0, 255) / 255.0
        m = random.randint(0, 255) / 255.0
        taraftar.shape("turtle")
        taraftar.color(k, y, m)
        taraftar.up()
        taraftar.goto(-90 + 25 * i, -120)
        taraftar.down()
        taraftar.left(90)

    x_birinci = 0
    x_ikinci = 0
    x_ucuncu = 0

    kazanan = input("Hangi kablumbağa kazanacak:")
    yazi = turtle.Turtle()
    yazi.up()
    yazi.goto(-120, 120)
    yazi.write(kazanan + " kablumbağanın kazanacağını düşünüyorsunuz ")

    while True:
        if x_birinci > 305 or x_ikinci > 305 or x_ucuncu > 305:
            break

        birinci_adim = random.randint(1, 5)
        x_birinci = x_birinci + birinci_adim
        birinci.forward(birinci_adim)

        ikinci_adim = random.randint(1, 5)
        x_ikinci = x_ikinci + ikinci_adim
        ikinci.forward(ikinci_adim)

        ucuncu_adim = random.randint(1, 5)
        x_ucuncu = x_ucuncu + ucuncu_adim
        ucuncu.forward(ucuncu_adim)

    if x_birinci > 305:
        t.write("Kırmızı Kazandı!")
    elif x_ikinci > 305:
        t.write("Mavi Kazandı!")
    elif x_ucuncu > 305:
        t.write("Sarı Kazandı!")

    input()

if s == "2":
    import json
    import os
    
    try:
        from termcolor import cprint # type: ignore
    except ImportError:
        def cprint(*args, **kwargs):
            print(*args)
    
    kelimeler = ["vantilatör", "adaptör", "kalem", "fare", "telefon", "kulaklık", "pervane", "merdane", "kestane"]
    
    
    def oyun_hazirlik():
        """Oyun için gerekli değişkenleri tanımlar"""
        global secilen_kelime, gorunen_kelime, can
        import random
        secilen_kelime = random.choice(kelimeler)
        gorunen_kelime = ["-"] * len(secilen_kelime)
        can = 5
    
    
    def harf_al():
        """Kullanıcıdan bir harf alır, alana kadar gerekirse hata verir, birisi quit yazarsa programı kapatır"""
        devam = True
        while devam:
            harf = input("Bir harf giriniz: ")
            if harf.lower() == "quit":
                cprint("Gidiyor gönlümün efendisi...", color="red", on_color="on_blue")
                exit()
            elif len(harf) == 1 and harf.isalpha() and harf not in gorunen_kelime:
                devam = False
            else:
                cprint("Hatalı Giriş", color="red", on_color="on_grey")
    
        # noinspection PyUnboundLocalVariable
        return harf.lower()
    
    
    def oyun_dongusu():
        """Oyunun ana döngüsü, harf alır, tutarsa görünen karakterler listesi güncellenir,
        tutmazsa can azaltılır, ve bu can bitene kadar ya da kelime bilinene kadar devam eder..."""
        global gorunen_kelime, can
        while can > 0 and secilen_kelime != "".join(gorunen_kelime):
            cprint("kelime: " + "".join(gorunen_kelime), color="cyan", attrs=["bold"])
            cprint("can   : <" + "❤" * can + " " * (5 - can) + ">", color="cyan", attrs=["bold"])
    
            girilen_harf = harf_al()
            pozisyonlar = harf_kontrol(girilen_harf)
            if pozisyonlar:
                for p in pozisyonlar:
                    gorunen_kelime[p] = girilen_harf
            else:
                can -= 1
    
    
    def harf_kontrol(girilen_harf):
        """Gelen harfin seçilen kelimede nerelerde olduğunu bulur"""
        poz = []
        for index, h in enumerate(secilen_kelime):
            if h == girilen_harf:
                poz.append(index)
        return poz
    
    
    def skor_tablosunu_goster():
        """Skor tablosunu gösterir"""
        veri = ayar_oku()
        cprint("|Skor\t\tKullanıcı|", color="white", on_color="on_grey")
        cprint("|------------------------|", color="white", on_color="on_grey")
        for skor, kullanici in veri["skorlar"]:
            cprint("|"+str(skor) +"\t\t"+ kullanici+" "*(9-len(kullanici))+"|", color="white", on_color="on_grey")
        cprint("|------------------------|", color="white", on_color="on_grey")
    
    
    def skor_tablosunu_guncelle():
        """Skor tablosunu son kullanıcının ismiyle ve skoruyla günceller"""
        veri = ayar_oku()
        veri["skorlar"].append((can, veri["son_kullanan"]))
        veri["skorlar"].sort(key=lambda skor_tuplei: skor_tuplei[0], reverse=True)
        veri["skorlar"] = veri["skorlar"][:5]
        ayar_yaz(veri)
    
    
    def oyun_sonucu():
        """Oyun bittiğinde kazanıp kazanamadığımızı ekrana yazar."""
        if can > 0:
            cprint("Kazandınız", color="yellow", on_color="on_red")
            skor_tablosunu_guncelle()
        else:
            cprint("Kaybettiniz", color="red", on_color="on_yellow")
        skor_tablosunu_goster()
    
    
    def dosyay_kontrol_et_yoksa_olustur():
        """Ayar dosyası var mı kontrol eder, varsa sağlam mı diye bakar,
        bozuk ya da olmayan durum için dosyayı öntanımlı değerlerle oluşturur"""
        yaz = False
        if os.path.exists("ayarlar.json"):
            try:
                ayar_oku()
            except ValueError as e:
                cprint("Hata: ValueError(" + ",".join(e.args) + ")", color="red", on_color="on_blue", attrs=["bold"])
                os.remove("ayarlar.json")
                yaz = True
        else:
            yaz = True
    
        if yaz:
            ayar_yaz({"skorlar": [], "son_kullanan": ""})
    
    
    def ayar_oku():
        """Ayarlar dosyasını okur"""
        with open("ayarlar.json") as f:
            return json.load(f)
    
    
    def ayar_yaz(veri):
        """Ayarlar dosyasına gönderilen veriyi yazar"""
        with open("ayarlar.json", "w") as f:
            json.dump(veri, f)
    
    
    def kullanici_adini_guncelle():
        """Kullanıcıdan isim alıp ayarlara yazdırmaya gönderir"""
        veri = ayar_oku()
        veri["son_kullanan"] = input("Kullanıcı Adınız: ")
        while not veri["son_kullanan"] or len(veri["son_kullanan"]) > 9:
            veri["son_kullanan"] = input("lykpython ile 9 karakter uzunluğunda yazın: ")
        ayar_yaz(veri)
    
    
    def kullanici_kontrol():
        """Bir önce giriş yapan kullanıcı ismini gösterip kullanıcıya bu siz misiniz diye sorar"""
        veri = ayar_oku()
        print("Son giriş yapan: " + veri["son_kullanan"])
        if not veri["son_kullanan"]:
            kullanici_adini_guncelle()
        elif input("Bu siz misiniz?(e/h) ").lower() == "h":
            kullanici_adini_guncelle()
    
    
    def main():
        """Programın ana döngüsü, oyunun çalışmasından yükümlü"""
        tekrar_edecek_mi = True
        dosyay_kontrol_et_yoksa_olustur()
        cprint("Merhaba, Adam Asmacaya hoşgeldiniz.", color="cyan", on_color="on_magenta", attrs=["bold"])
        cprint("Yardım: Oyun sırasında quit diyerek çıkabilirsiniz", color="cyan", on_color="on_magenta", attrs=["bold"])
        cprint("-"*30, color="cyan", on_color="on_magenta", attrs=["bold"])
        skor_tablosunu_goster()
        kullanici_kontrol()
        while tekrar_edecek_mi:
            oyun_hazirlik()
            oyun_dongusu()
            oyun_sonucu()
            if input("Devam?(e/h) ").lower() == "h":
                tekrar_edecek_mi = False
        cprint("Gidiyor gönlümün efendisi...", color="red", on_color="on_blue")
    
    main()
    
if s == "3":
    import random

    def play_game():
        choices = ['Taş', 'Kağıt', 'Makas']
        
        while True:
            # Kullanıcının seçimini al
            user_choice = input("Taş, Kağıt veya Makas? (Çıkmak için 'q' tuşuna basın): ")
            user_choice = user_choice.lower()
            
            if user_choice == 'q':
                print("Oyun sonlandırıldı.")
                break
            
            if user_choice not in choices:
                print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
                continue
            
            # Bilgisayarın seçimini belirle
            computer_choice = random.choice(choices)
            
            print(f"Senin seçimin: {user_choice}")
            print(f"Bilgisayarın seçimi: {computer_choice}")
            
            # Oyun sonucunu kontrol et
            if user_choice == computer_choice:
                print("Berabere! Tekrar deneyin.")
            elif (
                (user_choice == 'taş' and computer_choice == 'Makas') or
                (user_choice == 'kağıt' and computer_choice == 'Taş') or
                (user_choice == 'makas' and computer_choice == 'Kağıt')
            ):
                print("Tebrikler! Kazandınız.")
            else:
                print("Üzgünüm! Kaybettiniz.")

    # Oyunu oynat
    play_game()
    #Bu kodda, kullanıcıdan taş, kağıt veya makas seçimini alıyoruz. Bilgisayarın seçimini rastgele olarak belirliyoruz. Ardından, kullanıcının seçimini ve bilgisayarın seçimini ekrana yazdırıyoruz. Son olarak, kullanıcının seçimine göre oyun sonucunu kontrol edip ekrana yazdırıyoruz. Oyunu çıkmak için 'q' tuşuna basarak sonlandırabilirsiniz.

    #Bu kod sadece basit bir Taş Kağıt Makas oyunudur ve geliştirilebilir. Örneğin, puanlama sistemi ekleyebilir veya oyunun bir süre sınırlaması olabilir. Oyunu istediğiniz şekilde özelleştirebilirsiniz. Biz burada her taş kağıt makas sonrası kazanan tarafın skoruna 1 puan yazdırıp, 10 puana ulaşıldığında oyun sonlandırılmasını sağlayacak şeklinde oyunu güncelleyeceğiz. Güncel kodlarımız şu şekilde olur:

    import random

    def play_game():
        choices = ['Taş', 'Kağıt', 'Makas']
        user_score = 0
        computer_score = 0
        
        while True:
            # Kullanıcının seçimini al
            user_choice = input("Taş, Kağıt veya Makas? (Çıkmak için 'q' tuşuna basın): ")
            user_choice = user_choice.lower()
            
            if user_choice == 'q':
                print("Oyun sonlandırıldı.")
                break
            
            if user_choice not in choices:
                print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
                continue
            
            # Bilgisayarın seçimini belirle
            computer_choice = random.choice(choices)
            
            print(f"Senin seçimin: {user_choice}")
            print(f"Bilgisayarın seçimi: {computer_choice}")
            
            # Oyun sonucunu kontrol et
            if user_choice == computer_choice:
                print("Berabere! Tekrar deneyin.")
            elif (
                (user_choice == 'taş' and computer_choice == 'Makas') or
                (user_choice == 'kağıt' and computer_choice == 'Taş') or
                (user_choice == 'makas' and computer_choice == 'Kağıt')
            ):
                print("Tebrikler! Kazandınız.")
                user_score += 1
            else:
                print("Üzgünüm! Kaybettiniz.")
                computer_score += 1
            
            print(f"Puan Durumu: Sen {user_score} - {computer_score} Bilgisayar")
            
            # Oyunu kontrol et
            if user_score == 10:
                print("Oyun bitti. Tebrikler, Siz kazandınız!")
                break
            elif computer_score == 10:
                print("Oyun bitti. Üzgünüm, Bilgisayar kazandı.")
                break

    # Oyunu oynat
    play_game()
    #Eğer oyuncu ile bilgisayar arasındaki skor farkı 7 olduğunda (siz başka bir değer verebilirsiniz), yani bir tarafın 10 puana ulaşmayı beklemek zorunda kalmadan kazanan ilan edilmesini isterseniz, aşağıdaki gibi bir güncelleme yapabilirsiniz:

    import random

    def play_game():
        choices = ['Taş', 'Kağıt', 'Makas']
        user_score = 0
        computer_score = 0
        
        while True:
            # Kullanıcının seçimini al
            user_choice = input("Taş, Kağıt veya Makas? (Çıkmak için 'q' tuşuna basın): ")
            user_choice = user_choice.lower()
            
            if user_choice == 'q':
                print("Oyun sonlandırıldı.")
                break
            
            if user_choice not in choices:
                print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
                continue
            
            # Bilgisayarın seçimini belirle
            computer_choice = random.choice(choices)
            
            print(f"Senin seçimin: {user_choice}")
            print(f"Bilgisayarın seçimi: {computer_choice}")
            
            # Oyun sonucunu kontrol et
            if user_choice == computer_choice:
                print("Berabere! Tekrar deneyin.")
            elif (
                (user_choice == 'taş' and computer_choice == 'Makas') or
                (user_choice == 'kağıt' and computer_choice == 'Taş') or
                (user_choice == 'makas' and computer_choice == 'Kağıt')
            ):
                print("Tebrikler! Kazandınız.")
                user_score += 1
            else:
                print("Üzgünüm! Kaybettiniz.")
                computer_score += 1
            
            print(f"Puan Durumu: Sen {user_score} - {computer_score} Bilgisayar")
            
            # Oyunu kontrol et
            if abs(user_score - computer_score) == 7:
                if user_score > computer_score:
                    print("Oyun bitti. Tebrikler, Siz kazandınız!")
                else:
                    print("Oyun bitti. Üzgünüm, Bilgisayar kazandı.")
                break

    # Oyunu oynat
    play_game()