import csv
from datetime import datetime

class RiwayatTransaksi:
    def __init__(self, file_csv='transaksi.csv'):
        self.file_csv = file_csv
        self.transaksi_stack = []
        self.load_transaksi()

    def load_transaksi(self):
        try:
            with open(self.file_csv, newline='') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                for row in reader:
                    self.transaksi_stack.append(row)
        except FileNotFoundError:
            pass

    def catat_transaksi(self, id_transaksi, id_member, layanan, biaya):
        tanggal = datetime.now().strftime('%Y-%m-%d')
        data = [id_transaksi, id_member, tanggal, layanan, str(biaya)]
        self.transaksi_stack.append(data)
        with open(self.file_csv, 'a', newline='') as f:
            writer = csv.writer(f)
            if f.tell() == 0:
                writer.writerow(['id_transaksi', 'id_member', 'tanggal', 'layanan', 'biaya'])
            writer.writerow(data)
        print(f"Transaksi {id_transaksi} tercatat.")
