# Sistem Dispatching dan Manajemen Alokasi Hero Pada Agensi Penugasan Pahlawan

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

### 1. Pengujian Class `Hero`
Menguji pembuatan objek hero, pemanggilan *instance method* (`tampilkan_stats`), *static method* (`validasi_tipehero`), dan *class method* (`ubah_maksimal_tim`):

```python
hero1 = Hero("Invisigal", "Intelligence", 85, "Standby", 90)
hero2 = Hero("Blonde Blazer", "Power", 90, "Standby", 95)
hero3 = Hero("Coupe", "Mobility", 75, "Standby", 85)

# Instance Method
hero1.tampilkan_stats()
hero2.tampilkan_stats()

# Static Method
print(f"Tipe 'Intelligence' -> {Hero.validasi_tipehero('Intelligence')}")

# Class Method
Hero.ubah_maksimal_tim(4)
```

 ### 2. Pengujian Class `Misi`
Menguji pembuatan objek insiden/misi dan menampilkan detail informasinya (info_incident):
```python
inc1 = Misi("INC-01", "Penyelidikan Villain", "Downtown", ["Intelligence", "Mobility"], 150)
inc2 = Misi("INC-02", "Kebakaran Gedung", "Sector 7", ["Power"], 80)

# Instance Method
inc1.info_incident()
inc2.info_incident()
```

 ### 3. Pengujian Class `Dispatcher`
Menguji verifikasi kode akses, eksekusi dispatch hero ke lokasi misi, serta mekanisme perubahan status kesiapan hero:
```python
operator1 = Dispatcher("Player 1", "Night Shift", "Meja Utama 01", "PASS-1234")

# Verifikasi Kode Akses
operator1.verifikasi_kode_akses("PASS-1234")

# Eksekusi Dispatch Tim Hero
operator1.dispatch_tim_hero([hero1, hero3], inc1)


hero1.beristirahat()
hero1.tampilkan_stats()
```

 ### 4. Pengujian Setter dengan Data Valid
Menguji pembaruan nilai pada atribut privat melalui @setter menggunakan data yang memenuhi syarat validasi:
```python
hero2.persentase_sukses = 98
inc2.reputasi_reward = 120
```

### 5. Pengujian Setter dengan Data Tidak Valid (Exception Handling)
Menguji ketahanan program menggunakan blok try-except saat diberi input yang melanggar aturan validasi (misal: nilai di luar batas rentang, tipe data salah, angka bernilai negatif/nol):
```python
try:
    hero2.persentase_sukses = 150
except ValueError as e:
    print(f"[TERTANGKAP ERROR] {e}")

try:
    hero2.persentase_sukses = "Sangat Tinggi"
except ValueError as e:
    print(f"[TERTANGKAP ERROR] {e}")

try:
    operator1.total_dispatch = -5
except ValueError as e:
    print(f"[TERTANGKAP ERROR] {e}")

try:
    inc2.reputasi_reward = 0
except ValueError as e:
    print(f"[TERTANGKAP ERROR] {e}")
    ```
--------------------------------------------------------------------------------------------------------------------------------------
```
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