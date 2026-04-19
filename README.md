# 📚 Struktur Data – UTS
## Sistem Antrian Rumah Sakit (queue)

---

## 👤 Identitas Kelompok

| NIM | Nama        | Kelas        | Akun Github   |
|----|-------------|--------------------|----------|
| 2501010004  | Dewa Gede Agung Dwi Angga Suputra  | A       | BebekTerbang334     |
| 2501010018  | Dewa Gede Maha Putra  | A  |  Doremika452 |
| 2501010052  | I Kadek Cri Bhaskara Wirawan Sutha   | A          | Keydak  |


---


# 🎯 Rumusan Masalah

> 1. Bagaimana cara mengimplementasikan konsep queue (FIFO) dalam sistem antrian pasien di rumah sakit menggunakan OOP?
**Jawaban:**


Konsep queue (FIFO) diimplementasikan dengan menggunakan struktur data list, di mana pasien yang datang pertama akan dilayani terlebih dahulu. Dalam OOP, dibuat sebuah class (misalnya `AntrianRumahSakit`) yang memiliki atribut antrian dan method seperti `tambah_pasien()` untuk menambah data ke belakang antrian dan `panggil_pasien()` untuk mengambil data dari depan antrian menggunakan `pop(0)`.

> 2. Bagaimana sistem dapat mengelola proses penambahan, pemanggilan, dan penampilan data antrian pasien secara efektif?

Sistem mengelola antrian dengan menyediakan beberapa method utama, yaitu:

* `tambah_pasien()` untuk menambahkan pasien ke antrian
* `panggil_pasien()` untuk memanggil pasien sesuai urutan
* `lihat_antrian()` untuk menampilkan seluruh daftar antrian
  Dengan pembagian fungsi ini, pengelolaan data menjadi lebih terstruktur, mudah dipahami, dan efisien.
  
> 3. Bagaimana sistem dapat memberikan informasi jumlah antrian dan urutan pasien secara akurat?

**Jawaban:**
Sistem menggunakan method `jumlah_antrian()` untuk menghitung jumlah pasien dalam antrian dengan fungsi `len()`. Sedangkan urutan pasien ditampilkan menggunakan perulangan (`enumerate`) pada method `lihat_antrian()`, sehingga setiap pasien memiliki nomor urut yang jelas dan akurat.

---

# 📖 Ringkasan Teori

## 1. Apa itu Struktur Data?

Dalam pemrograman, struktur data memiliki peran penting dalam menentukan kinerja program, kompleksitas kode, serta efisiensi penggunaan sumber daya komputer. Pemilihan struktur data yang tepat akan mempermudah proses pengolahan, pencarian, dan penyimpanan data.

Menurut Herawan (2022), struktur data adalah cara mengorganisasi dan menyimpan data dalam komputer yang dapat mempengaruhi kinerja program dan efisiensi penggunaan sumber daya.

Struktur data juga dapat dipahami sebagai metode penyimpanan dan pengaturan data secara terstruktur dalam sistem komputer agar mempermudah proses akses dan pengolahan data (“Artikel Struktur Data, Audit dan Jaringan Komputer,” 2018).

Selain itu, dalam teknik pemrograman, struktur data merujuk pada tata letak data yang terdiri dari kolom dan baris (record), baik yang terlihat oleh pengguna maupun yang digunakan untuk kebutuhan internal sistem (Jodi, 2024).


📚 Referensi:
- Herawan, B. (2022). Buku Algoritma dan Struktur Data.  
- “Artikel Struktur Data, Audit dan Jaringan Komputer.” (2018).  
- Jodi, I. D. (2024). Algoritma dan Struktur Data.
