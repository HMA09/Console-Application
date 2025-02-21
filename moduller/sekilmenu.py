

def sekiller():
    
    print("╔═════════════════════╗")
    print("║ ŞEKİL ÇİZDİRME      ║")
    print("║                     ║")
    print("║  1-Sağa Ok          ║")
    print("║  2-Sola Ok          ║")
    print("║  3-Kare             ║")
    print("║  4-Dikdörtgen       ║")
    print("║  5-Üçgen            ║")
    print("║  6-Geometrik Şekil  ║")
    print("║  7-Ortaya Karışık   ║")
    print("║  8-Çıkış            ║")
    print("║                     ║")
    print("║    Seçimini yap     ║")
    print("╚═════════════════════╝")

    s=input("Seçiminizi Yapınız:")


    if s == "1":
        print("Sağa Ok")
        import turtle
        turtle.forward(100)
        input()
    if s == "2":
        print("Sola Ok")
        import turtle
        turtle.right(180)
        turtle.forward(100)
        input()
    if s == "3":
        print("Kare")
        import turtle
        for a in range (4):
            turtle.forward(100)
            turtle.right(90)
        input()
    if s == "4":
        print("Dikdörtgen")
        import turtle
        for a in range (2):
            turtle.forward(150)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(90)
        input()
    if s == "5":
        print("Üçgen")
        import turtle
        turtle.right(60)
        turtle.forward(100)
        turtle.right(120)
        turtle.forward(100)
        turtle.right(120)
        turtle.forward(100)
        input()
    if s == "6":
        print("Geometrik Şekil")
        import turtle
        turtle.speed(10)
        for a in range (24):
            for a in range (4):
                turtle.forward(100)
                turtle.right(90)
            turtle.right(15)
        input()
    if s == "7":
        print("Square Spiral")
        import turtle
        turtle.speed(10)
        t = turtle.Pen()
        for x in range(100):
            t.forward(x)
            t.left(91)
        input()
    if s == "8":
        exit()
 
sekiller()
