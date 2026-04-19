# 📚 Struktur Data – UTS
## Sistem Antrian Rumah Sakit (queue)

Link PPT :
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

## 2. Konsep Queue

Menurut Rizaldy Gunawan, H. Yuana, dan S. Kirom. (2023) Queue atau antrian merupakan salah satu struktur data yang bekerja dengan prinsip FIFO (First In First Out), yaitu elemen yang pertama kali masuk akan menjadi elemen pertama yang keluar. Dalam implementasinya, antrian memiliki dua operasi utama, yaitu enqueue untuk menambahkan elemen ke dalam antrian dan dequeue untuk menghapus elemen dari antrian. Struktur antrian ini dapat diimplementasikan menggunakan linear array maupun circular array tergantung pada kebutuhan sistem dan efisiensi pengelolaan memori.

Menurut Mayangsari dan Prastiwi, (2016) model antrian (queueing model) merupakan pendekatan matematis yang digunakan untuk menganalisis sistem pelayanan, khususnya dalam memahami perilaku antrian. Tujuan utama dari model ini adalah meminimalkan total biaya, baik biaya langsung dalam penyediaan fasilitas layanan maupun biaya tidak langsung akibat waktu tunggu pelanggan. Selain itu, model antrian juga digunakan untuk memprediksi kinerja sistem, seperti jumlah pelanggan dalam antrian, waktu tunggu, waktu pelayanan, serta tingkat utilisasi server.

Lestari (2018) mengatakan dalam penerapan sistem antrean, pemilihan struktur data yang tepat sangat penting untuk menjaga keadilan dan keteraturan layanan. Struktur data queue dengan prinsip FIFO dianggap paling ideal karena memastikan bahwa setiap elemen diproses sesuai urutan kedatangannya. Untuk meningkatkan fleksibilitas, penggunaan linked list sering dipilih karena mampu menyesuaikan ukuran antrian secara dinamis tanpa batas kapasitas awal seperti pada array. Hal ini menjadikan sistem lebih efisien dalam menangani perubahan jumlah data secara terus-menerus.

📚 Referensi:
- Rizaldy Gunawan, H. Yuana, & S. Kirom, 2023.
- Mayangsari & Prastiwi, 2016; Darmawan et al., 2023. 
- Lestari, 2018; Dewi, 2020.
