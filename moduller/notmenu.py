def noth():
    print("Not Hesaplama Robotu")
    vize = int(input("Vize Notunuzu Giriniz:"))
    final = int(input("Final Notunuzu Giriniz:"))
    ort = (vize*0.4) + (final*0.6)
    print("Ortalamanız:", ort)
    if ort >= 90:
        print("AA")
    elif ort >= 85:
        print("BA")
    elif ort >= 80:
        print("BB")
    elif ort >= 75:
        print("CB")
    elif ort >= 70:
        print("CC")
    elif ort >= 65:
        print("DC")
    elif ort >= 60:
        print("DD")
    elif ort >= 55:
        print("FD")
    else:
        print("FF")
noth()