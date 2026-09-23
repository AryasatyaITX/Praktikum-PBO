# Sistem Dispatching dan Manajemen Alokasi Hero

Program aplikasi konsol berbasis Python untuk mengelola dan memproses pengiriman (*dispatch*) superhero pada sebuah agensi penugasan pahlawan. Program ini menerapkan prinsip Pemrograman Berbasis Objek (OOP) seperti Enkapsulasi, Properties, serta penggunaan berbagai jenis Method.

===============================================================================================================================================

## Ringkasan Penjelasan Program

Program ini dibuat untuk mensimulasikan alur kerja operasional agensi hero. Penjelasan singkat mengenai sistem yang diimplementasikan:

1. **Manajemen Hero (`Hero`)**: Menyimpan data identitas, status kesiapan (*Standby/Resting*), serta statistik keberhasilan hero secara privat. Terdapat mekanisme pemulihan status melalui fungsi beristirahat.
2. **Manajemen Operator (`Dispatcher`)**: Mengelola data operator dan mengeksekusi pengiriman tim hero ke lokasi insiden. Sistem memeriksa batas anggota tim, kesiapan status hero, dan kesesuaian tipe hero dengan kebutuhan misi.
3. **Manajemen Insiden (`Misi`)**: Menyimpan detail panggilan darurat, lokasi, kriteria kualifikasi tim, dan reward reputasi.
4. **Enkapsulasi & Validasi Data**: Data sensitif (seperti persentase sukses, total dispatch, dan reward reputasi) dilindungi menggunakan hak akses privat dan diakses melalui `@property` & `@setter` dengan penanganan validasi input (error handling).

============================================================================================================================================

## Fitur Utama Program

Program menjalankan simulasi otomatis yang mencakup fungsi-fungsi berikut:
* **Pengelolaan Data Hero:** Penambahan data hero, validasi kualifikasi tipe, dan reset daftar hero terdaftar.
* **Pengelolaan Misi & Dispatch:** Pemrosesan tim hero untuk menjalankan misi berdasarkan kecocokan tipe dan status kesiapan.
* **Manajemen Status Hero:** Perubahan status otomatis menjadi *Resting* setelah misi (atau saat kriteria gagal) serta pemulihan status kembali ke *Standby*.
* **Verifikasi Operator:** Pengecekan kode akses/password untuk autentikasi operator dispatcher.
* **Validasi & Exception Handling:** Pengujian getter/setter menggunakan data valid maupun data tidak valid dengan penanganan error `try-except`.

------------------------------------------------------------------------------------------------------------------------------------------------

## Struktur Kode & Kelas

Program terdiri dari tiga kelas utama yang saling berinteraksi:

1. **`Hero`**: Kelas model untuk entitas pahlawan. Berisi atribut profil, status kesiapan, serta method untuk menampilkan statistik, beristirahat, mereset counter hero terdaftar (`@classmethod`), dan memvalidasi tipe hero (`@staticmethod`).
2. **`Dispatcher`**: Kelas pengelola operasi. Berisi data operator, fungsi verifikasi kode akses, serta logika utama `dispatch_tim_hero` untuk memproses penugasan tim pahlawan ke lokasi insiden.
3. **`Misi`**: Kelas model untuk entitas insiden/panggilan darurat. Mengelola detail lokasi, syarat tipe hero yang dibutuhkan, dan poin reward reputasi.

-----------------------------------------------------------------------------------------------------------------------------------------------

## Pengujian Program

Pengujian dilakukan langsung pada bagian *main code* dengan skenario sebagai berikut:

1. **Pengujian Class `Hero`**: Membuat 3 objek hero, menampilkan statistik (`tampilkan_stats()`), memvalidasi tipe hero dengan static method (`validasi_tipehero()`), dan mereset counter hero dengan class method (`reset_daftar()`).
2. **Pengujian Class `Misi`**: Membuat 2 objek misi/insiden dan menampilkan detail informasi misi (`info_incident()`).
3. **Pengujian Class `Dispatcher` & Interaksi Objek**: 
   * Membuat objek operator dan menampilkan datanya (`info_operator()`).
   * Melakukan verifikasi password (`verifikasi_kode_akses()`).
   * Memproses penugasan tim hero ke lokasi misi (`dispatch_tim_hero()`).
   * Menguji perubahan status hero menjadi *Resting* setelah misi serta memulihkannya kembali menjadi *Standby* (`beristirahat()`).
4. **Pengujian Setter Data Valid**: Mengubah atribut privat (`persentase_sukses`, `reputasi_reward`, `total_dispatch`) menggunakan nilai yang memenuhi syarat validasi.
5. **Pengujian Setter Data Tidak Valid (Exception Handling)**: Menguji ketahanan program dengan memasukkan data tidak valid (nilai melebihi batas, tipe data salah, angka negatif/nol) menggunakan blok `try-except` untuk memastikan error berhasil ditangkap dengan baik.

--------------------------------------------------------------------------------------------------------------------------------------

## Persyaratan Sistem

Untuk menjalankan program ini, pastikan sistem Anda telah terinstal:
* **Python** versi 3.8 atau yang lebih baru.

--------------------------------------------------------------------------------------------------------------------------------------

## Cara Menjalankan Program

1. Simpan kode program ke dalam sebuah file bernama `main.py`.
2. Buka terminal atau Command Prompt (CMD), lalu arahkan direktori ke lokasi file `main.py` disimpan.
3. Jalankan program dengan perintah berikut:
   ```bash
   python main.py