import os
from tabulate import tabulate


class AntrianRumahSakit:
    def __init__(self):
        self.antrian = []

  
    def jumlah_antrian(self):
        return len(self.antrian)

     #enqueue
    def tambah_pasien(self, nama_pasien):
        self.antrian.append(nama_pasien)
        print(f"Pasien '{nama_pasien}' ditambahkan ke antrian.")
        
    #peek    
    def cek_antrian_selanjutnya(self):
        if not self.antrian:
            print("Antrian kosong.")
        else:
            print(f"Pasien berikutnya: {self.antrian[0]}")

    # FIFO & #dequeue
    def panggil_pasien(self):
        if not self.antrian:
            print('Antrian kosong, tidak ada pasien.')
        else:
            pasien = self.antrian.pop(0)
            print(f"Memanggil pasien: {pasien}")
                         
    #display
    def lihat_antrian(self):
        if not self.antrian:
            print("Antrian kosong.")
        else:
            print("Daftar antrian pasien:")
            data = [[i, pasien]
                    for i, pasien in enumerate(self.antrian, start=1)]
            print(tabulate(data, headers=[
                  "No", "Nama Pasien"], tablefmt="psql"))


antrian_rs = AntrianRumahSakit()

while True:
    os.system("cls")
    print("\n=== Sistem Antrian Rumah Sakit ===")
    print("1. Tambah Pasien")
    print("2. Lihat Semua Pasien")
    print("3. Cek Antrian Terdepan")
    print("4. Panggil Pasien")
    print("5. Keluar")
    print("=======================")
    pilihan = input("Pilih menu: ")
    print("=======================")

    if pilihan == "1":
        nama = input("Masukkan nama pasien: ")
        antrian_rs.tambah_pasien(nama)
        print("=======================")
        while True:
            pilihan1 = input("Ingin menginput pasien lagi? (yes/no) : ")

            if pilihan1 == "yes":
                nama = input("Masukkan nama pasien: ")
                antrian_rs.tambah_pasien(nama)
            elif pilihan1 == "no":

                break
            else:
                print("Pilihan tidak valid.")
    elif pilihan == "2":
        antrian_rs.lihat_antrian()
        input("\nTekan Enter untuk lanjut...")
    elif pilihan == "3":
        antrian_rs.cek_antrian_selanjutnya()
        input("\nTekan Enter untuk lanjut...")
    elif pilihan == "4":
        antrian_rs.panggil_pasien()
        input("\nTekan Enter untuk lanjut...")
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")
        input("\nTekan Enter untuk lanjut...")
