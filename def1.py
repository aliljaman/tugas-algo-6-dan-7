def kabisat(tahun):
    return tahun % 4 == 0


def hari(bulan, tahun):
    if bulan == 2:
        if kabisat(tahun):
            return 29
        else:
            return 28
    elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
        return 30
    else:
        return 31


while True:
    bulan = int(input("Masukkan bulan (1-12): "))

    if bulan == 0:
        break

    tahun = int(input("Masukkan tahun: "))

    print(hari(bulan, tahun), "hari dalam sebulan")
