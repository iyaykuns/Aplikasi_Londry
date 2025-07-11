import csv

class ManajemenMember:
    def __init__(self, file_csv='member.csv'):
        self.file_csv = file_csv
        self.data_member = {}  # HashMap
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_csv, newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.data_member[row['id_member']] = row
        except FileNotFoundError:
            pass

    def simpan_data(self):
        with open(self.file_csv, 'w', newline='') as f:
            fieldnames = ['id_member', 'nama', 'no_hp', 'alamat', 'saldo']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for data in self.data_member.values():
                writer.writerow(data)

    def tambah_member(self, id_member, nama, no_hp, alamat, saldo):
        self.data_member[id_member] = {
            'id_member': id_member,
            'nama': nama,
            'no_hp': no_hp,
            'alamat': alamat,
            'saldo': str(saldo)
        }
        self.simpan_data()
        print(f"Member {nama} berhasil ditambahkan.")
