def kurmenu():
   
    print("╔═════════════════════╗")
    print("║ DÖVİZ HESAPLAMA     ║")
    print("║                     ║")
    print("║  1-Dolar/TL         ║")
    print("║  2-Euro/TL          ║")
    print("║  3-Çıkış            ║")
    print("║                     ║")
    print("║    Seçimini yap     ║")
    print("╚═════════════════════╝")

    s=input("Seçiminizi Yapınız:")
        
    if s == "1":
        print("Dolar Kuru")
        print("Güncel Dolar Kuru: 36.53")
        s1 = int(input("Çevirmek İstediğiniz Dolar Miktarını Giriniz:"))
        print("Sonuç:", s1*36.53 , "TL")
    if s == "2":
        print("Euro Kuru")
        print("Güncel Euro Kuru: 37.32")
        s1 = int(input("Çevirmek İstediğiniz Euro Miktarını Giriniz:"))
        print("Sonuç:", s1*37.32, "TL")
    if s == "3":
        exit()  
kurmenu()