def prima(angka):
    if angka <= 1:
        return False

    for i in range(2, angka):
        if angka % i == 0:
            return False

    return True


def hasil(angka):
    if prima(angka):
        print(angka, "adalah bilangan Prima")
    else:
        print(angka, "bukanlah bilangan Prima")


angka = int(input("Masukkan angka: "))
hasil(angka)