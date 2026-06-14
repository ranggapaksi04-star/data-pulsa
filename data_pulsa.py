data_pulsa = []

def tambah_data():
    tanggal = input("Masukkan tanggal (dd-mm-yyyy): ")
    nomor = input("Masukkan nomor tujuan: ")
    nominal = int(input("Masukkan nominal pulsa: "))
    harga = int(input("Masukkan harga pulsa: "))

    data = {
        "tanggal": tanggal,
        "nomor": nomor,
        "nominal": nominal,
        "harga": harga
    }

    data_pulsa.append(data)
    print("Data pembelian pulsa berhasil ditambahkan!\n")

def tampil_data():
    if len(data_pulsa) == 0:
        print("Data masih kosong.\n")
    else:
        print("=== Riwayat Pembelian Pulsa ===")
        for i, d in enumerate(data_pulsa, start=1):
            print(f"{i}. Tanggal  : {d['tanggal']}")
            print(f"   Nomor    : {d['nomor']}")
            print(f"   Nominal  : {d['nominal']}")
            print(f"   Harga    : {d['harga']}")
            print("---------------------------")
        print()

def cari_data():
    cari = input("Masukkan nomor tujuan yang dicari: ")
    ditemukan = False

    for d in data_pulsa:
        if d["nomor"] == cari:
            print("Data ditemukan:")
            print(d)
            ditemukan = True

    if not ditemukan:
        print("Data tidak ditemukan.\n")

def total_pengeluaran():
    total = sum(d["harga"] for d in data_pulsa)
    print(f"Total pengeluaran pulsa: Rp{total}\n")

while True:
    print("=== MENU RIWAYAT PEMBELIAN PULSA ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Cari Data")
    print("4. Total Pengeluaran")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampil_data()
    elif pilihan == "3":
        cari_data()
    elif pilihan == "4":
        total_pengeluaran()
    elif pilihan == "5":
        print("Terima kasih.")
        break
    else:
        print("Pilihan tidak valid.\n")