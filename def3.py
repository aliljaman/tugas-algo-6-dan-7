def ordinal(angka):
    if angka % 100 == 11 or angka % 100 == 12 or angka % 100 == 13:
        return str(angka) + "th"
    elif angka % 10 == 1:
        return str(angka) + "st"
    elif angka % 10 == 2:
        return str(angka) + "nd"
    elif angka % 10 == 3:
        return str(angka) + "rd"
    else:
        return str(angka) + "th"


while True:
    angka = int(input("Masukkan angka: "))

    if angka == 0:
        print("Terima kasih")
        break

    print(ordinal(angka))