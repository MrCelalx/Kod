def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "S�f�ra b�lme hatas�!"
    return x / y

while True:
    print("Yapmak istedi�iniz i�lemi se�in:")
    print("1.Toplama")
    print("2.��karma")
    print("3.�arpma")
    print("4.B�lme")
    print("5.��k��")

    secim = input("Se�iminizi girin (1/2/3/4/5): ")

    if secim == '5':
        print("��k�yor...")
        break

    sayi1 = float(input("Birinci say�y� girin: "))
    sayi2 = float(input("�kinci say�y� girin: ")

    if secim == '1':
        print("Sonu�:", toplama(sayi1, sayi2))
    elif secim == '2':
        print("Sonu�:", cikarma(sayi1, sayi2))
    elif secim == '3':
        print("Sonu�:", carpma(sayi1, sayi2))
    elif secim == '4':
        print("Sonu�:", bolme(sayi1, sayi2))
    else:
        print("Ge�ersiz se�im! L�tfen tekrar deneyin.")