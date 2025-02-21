
def ritmik():
    print("Ritmik Sayma Robotu")
    B1 = int(input("Başlanıç Sayısını Giriniz: "))
    B2 = int(input("Bitiş Sayısını Giriniz: "))
    r1 = int(input("Ritmik Artışı Giriniz: "))
    print(*range(B1, B2, r1))

ritmik()