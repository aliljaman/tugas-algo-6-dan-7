def nilai_angka(huruf="A"):
    if huruf == "A":
        return 4
    elif huruf == "B":
        return 3
    elif huruf == "C":
        return 2
    elif huruf == "D":
        return 1
    else:
        return 0


total = 0
jumlah = 0

while True:
    huruf = input("Masukkan nilai: ").upper()

    if huruf == "":
        break

    angka = nilai_angka(huruf)

    print("Nilai =", angka)

    total = total + angka
    jumlah = jumlah + 1

if jumlah > 0:
    print("Rata-ratanya adalah:", total / jumlah) 