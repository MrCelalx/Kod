def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Sýfýra bölme hatasý!"
    return x / y

while True:
    print("Yapmak istediðiniz iþlemi seçin:")
    print("1.Toplama")
    print("2.Çýkarma")
    print("3.Çarpma")
    print("4.Bölme")
    print("5.Çýkýþ")

    secim = input("Seçiminizi girin (1/2/3/4/5): ")

    if secim == '5':
        print("Çýkýyor...")
        break

    sayi1 = float(input("Birinci sayýyý girin: "))
    sayi2 = float(input("Ýkinci sayýyý girin: ")

    if secim == '1':
        print("Sonuç:", toplama(sayi1, sayi2))
    elif secim == '2':
        print("Sonuç:", cikarma(sayi1, sayi2))
    elif secim == '3':
        print("Sonuç:", carpma(sayi1, sayi2))
    elif secim == '4':
        print("Sonuç:", bolme(sayi1, sayi2))
    else:
        print("Geçersiz seçim! Lütfen tekrar deneyin.")