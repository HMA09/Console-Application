def hmmenu():
   
    print("╔═════════════════════╗")
    print("║ HESAP MAKİNESİ      ║")
    print("║                     ║")
    print("║  1-Toplama          ║")
    print("║  2-Çıkarma          ║")
    print("║  3-Çarpma           ║")
    print("║  4-Bölme            ║")
    print("║  5-Üs Alma          ║")
    print("║  6-Dörtgen Alanı    ║")
    print("║  7-Dörtgen Çevresi  ║")
    print("║  8-Çıkış            ║")
    print("║                     ║")
    print("║    Seçimini yap     ║")
    print("╚═════════════════════╝")

    s=input("Seçiminizi Yapınız:")
        
    if s == "1":
        print("TOPLAMA")
        s1 = int(input("1. Sayıyı Giriniz:"))
        s2 = int(input("2. Sayıyı Giriniz:"))
        print("Toplam:", s1+s2)
    if s == "2":
        print("ÇIKARMA")
        s1 = int(input("1. Sayıyı Giriniz:"))
        s2 = int(input("2. Sayıyı Giriniz:"))
        print("Fark:", s1-s2)
    if s == "3":
        print("ÇARPMA")
        s1 = int(input("1. Sayıyı Giriniz:"))
        s2 = int(input("2. Sayıyı Giriniz:"))
        print("Çarpım:", s1*s2)
    if s == "4":
        print("BÖLME")
        s1 = int(input("1. Sayıyı Giriniz:"))
        s2 = int(input("2. Sayıyı Giriniz:"))
        print("Bölüm:", s1/s2)
    if s == "5":
        print("ÜS ALMA")
        s1 = int(input("Üs Alınacak Sayıyı Giriniz:"))
        s2 = int(input("Üs Sayıyı Giriniz:"))
        print("Sonuç:", s1**s2)
    if s == "6":
        print("DÖRTGEN ALANI")
        s1 = int(input("Kısa Kenarını Giriniz:"))
        s2 = int(input("Uzun Kenarını Giriniz:"))
        print("Alan:", s1*s2)
    if s == "7":
        print("DÖRTGEN ÇEVRESİ")
        s1 = int(input("Kısa Kenarını Giriniz:"))
        s2 = int(input("Uzun Kenarını Giriniz:"))
        print("Çevresi:", (s1+s2)*2)
    if s == "8":
        exit()

hmmenu()