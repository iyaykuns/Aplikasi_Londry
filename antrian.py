import csv
from collections import deque
from datetime import datetime

class AntrianLaundry:
    def __init__(self, file_csv='antrian.csv'):
        self.file_csv = file_csv
        self.antrian = deque()
        self.load_antrian()

    def load_antrian(self):
        try:
            with open(self.file_csv, newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.antrian.append(row)
        except FileNotFoundError:
            pass

    def simpan_antrian(self):
        with open(self.file_csv, 'w', newline='') as f:
            fieldnames = ['id_antrian', 'id_member', 'layanan', 'waktu_masuk']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for item in self.antrian:
                writer.writerow(item)

    def tambah_antrian(self, id_antrian, id_member, layanan):
        waktu = datetime.now().strftime('%Y-%m-%d %H:%M')
        data = {
            'id_antrian': id_antrian,
            'id_member': id_member,
            'layanan': layanan,
            'waktu_masuk': waktu
        }
        self.antrian.append(data)
        self.simpan_antrian()
        print(f"Antrian {id_antrian} ditambahkan.")
