def anamenu():
    print("╔════════════════════════╗")
    print("║   Konsol Uygulaması    ║")
    print("║1-HESAP MAKİNESİ        ║")
    print("║2-OYUNLAR               ║")
    print("║3-ŞEKİL ÇİZDİRME        ║")
    print("║4-RİTMİK SAYMA          ║")
    print("║5-NOT HESAPLAMA         ║")
    print("║6-ÇARPIM TABLOSU        ║")
    print("║7-DÖVİZ UYGULAMASI      ║")
    print("║8-SICAKLIK ÇEVİRME      ║")
    print("║9-ÇIKIŞ (e)             ║")
    print("║    Seçimini Yap        ║")
    print("╚════════════════════════╝")

    secim = input("Seçiminizi Yapınız: ")
    if secim == "1":
        import moduller.hesapmakinesi
        moduller.hesapmakinesi.hmmenu()
    elif secim == "2":
        import moduller.oyunmenu
        moduller.oyunmenu.oyun()
    elif secim == "3":
        import moduller.sekilmenu
        moduller.sekilmenu.sekiller()
    elif secim == "4":
        import moduller.Ritmikmenu
        moduller.Ritmikmenu.ritmik()
    elif secim == "5":
        import moduller.notmenu
        moduller.notmenu.not_hesapla()
    elif secim == "6":
        import moduller.carpimtablosu
        moduller.carpimtablosu.carpim()
    elif secim == "7":
        import moduller.Dovizmenu
        moduller.Dovizmenu.kurmenu()
    elif secim == "8":
        import moduller.sicaklikmenu
        moduller.sicaklikmenu.derece()
    elif secim == "9":
        exit()
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
        anamenu()

anamenu()