def format_alamat(nama_jalan, rt_rw, kelurahan, kecamatan, kota, provinsi, kode_pos):
    alamat = (
        f"Alamat lengkap: Jalan {nama_jalan}, RT/RW {rt_rw}, "
        f"Kelurahan {kelurahan}, Kecamatan {kecamatan}, "
        f"Kota {kota}, Kode Pos {kode_pos}."
    )
    return alamat

def main():
    print("=== Masukkan Data Alamat Anda ===")
    nama_jalan = input("Nama Jalan       : ")
    rt_rw = input("RT/RW (contoh: 001/002): ")
    kelurahan = input("Kelurahan        : ")
    kecamatan = input("Kecamatan        : ")
    kota = input("Kota/Kabupaten   : ")
    provinsi = input("Provinsi         : ")
    kode_pos = input("Kode Pos         : ")

    alamat = format_alamat(nama_jalan, rt_rw, kelurahan, kecamatan, kota, provinsi, kode_pos)
    print("\n" + "=" * 40)
    hasil = format_alamat(
        nama_jalan, rt_rw, kelurahan, kecamatan, kota, provinsi, kode_pos
    )
    print(hasil)
    print("=" * 40)


if __name__ == "__main__":
    main()