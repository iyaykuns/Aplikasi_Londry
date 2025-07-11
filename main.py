from member import ManajemenMember
from transaksi import RiwayatTransaksi
from antrian import AntrianLaundry

member = ManajemenMember()
transaksi = RiwayatTransaksi()
antrian = AntrianLaundry()

while True:
    print("\n=== SISTEM MEMBER LAUNDRY ===")
    print("1. Registrasi Member")
    print("2. Tambah Transaksi")
    print("3. Tambah Antrian")
    print("4. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == '1':
        id_member = input("ID Member: ")
        nama = input("Nama: ")
        no_hp = input("No HP: ")
        alamat = input("Alamat: ")
        saldo = int(input("Saldo Awal: "))
        member.tambah_member(id_member, nama, no_hp, alamat, saldo)

    elif pilih == '2':
        id_transaksi = input("ID Transaksi: ")
        id_member = input("ID Member: ")
        layanan = input("Layanan (Cuci/Kering/Setrika): ")
        biaya = int(input("Biaya: "))
        if id_member in member.data_member:
            saldo_sekarang = int(member.data_member[id_member]['saldo'])
            if saldo_sekarang >= biaya:
                member.data_member[id_member]['saldo'] = str(saldo_sekarang - biaya)
                member.simpan_data()
                transaksi.catat_transaksi(id_transaksi, id_member, layanan, biaya)
            else:
                print("Saldo tidak cukup.")
        else:
            print("Member tidak ditemukan.")

    elif pilih == '3':
        id_antrian = input("ID Antrian: ")
        id_member = input("ID Member: ")
        layanan = input("Layanan (Cuci/Kering/Setrika): ")
        antrian.tambah_antrian(id_antrian, id_member, layanan)

    elif pilih == '4':
        print("Terima kasih.")
        break

    else:
        print("Pilihan tidak valid.")
