# "Sistem Dispatching dan Manajemen Alokasi Hero pada Agensi Penugasan Pahlawan"


═════════════════════════════════════════════════════════════════════════════════════════════

## Deskripsi Program

Program ini mensimulasikan sistem manajemen dispatch superhero dan penugasan misi pada sebuah agensi.

Ia menerapkan konsep OOP, seperti class, object, attribute, method, encapsulation dan property. Terdapat juga fitur untuk menyimpan data hero, dispatcher (operator), dan misi.

Program dapat melakukan beberapa proses, yaitu:

1. Menambahkan dan menampilkan data hero.
2. Memvalidasi tipe hero dan mereset counter hero.
3. Menambahkan dan menampilkan data misi.
4. Menambahkan dan menampilkan data dispatcher.
5. Melakukan verifikasi kode akses operator.
6. Memproses dispatch tim hero untuk menjalankan misi.
7. Mengubah status hero menjadi resting setelah misi atau saat kriteria gagal.
8. Memulihkan status hero melalui fitur beristirahat.
9. Mengubah reward reputasi misi dan persentase sukses hero.
10. Menguji getter dan setter valid serta penanganan error (setter tidak valid).


═════════════════════════════════════════════════════════════════════════════════════════════

## Struktur Class
Program ini memiliki tiga class utama, yaitu:

### 1. Class `Hero`
Berfungsi untuk menyimpan data hero yang ada di agensi.

#### a. Class Attribute
- `total_hero` = Menyimpan jumlah seluruh objek hero yang dibuat.
- `nama_agency` = Menyimpan nama agensi default ("Phoenix Agency").
- `maksimal_tim_dispatch` = Batas maksimal hero dalam satu tim dispatch (3 hero).

#### b. Instance Attribute
- `nama` = Menyimpan nama hero.
- `tipe_hero` = Menyimpan tipe/kategori hero (misal: Intelligence, Power, Mobility).
- `power_level` = Menyimpan tingkat kekuatan hero.
- `status` = Menyimpan status kesiapan hero (Standby / Resting).
- `__persentase_sukses` = Menyimpan tingkat keberhasilan hero secara privat.

#### c. Method
- `__init__()` = Membuat objek hero dan mengisi data awal otomatis.
- `tampilkan_stats()` = Menampilkan statistik dan informasi hero.
- `beristirahat()` = Mengubah status hero dari "Resting" kembali menjadi "Standby".
- `reset_daftar()` = Class method untuk mereset counter `total_hero` menjadi 0.
- `validasi_tipehero()` = Static method untuk mengecek apakah tipe hero valid sesuai kriteria.
- `property persentase_sukses` = Getter, untuk mengambil nilai persentase sukses.
- `persentase_sukses.setter` = Setter, untuk mengubah persentase sukses dengan ketentuan berupa angka dan berada di rentang 0 - 100%.

___________________________________________

### 2. Class `Dispatcher`
Berfungsi untuk menyimpan data operator dan mengelola pengiriman tim hero.

#### a. Class Attribute
- `total_operator` = Menyimpan jumlah seluruh objek operator yang dibuat.
- `sistem_operasi` = Menyimpan nama OS dispatch.
- `pusat_komando` = Menyimpan lokasi pusat komando.

#### b. Instance Attribute
- `nama_operator` = Menyimpan nama operator dispatcher.
- `shift_aktif` = Menyimpan waktu shift kerja operator.
- `stasiun_kerja` = Menyimpan lokasi meja/stasiun kerja operator.
- `__kode_akses` = Menyimpan kode akses/password operator secara privat.
- `__total_dispatch` = Menyimpan total dispatch yang diproses secara privat.

#### c. Method
- `__init__()` = Membuat objek dispatcher dan mengisi data awal otomatis.
- `info_operator()` = Menampilkan informasi data operator.
- `verifikasi_kode_akses()` = Memeriksa kecocokan kode akses input dengan `__kode_akses`.
- `dispatch_tim_hero()` = Memproses pengiriman tim hero ke suatu misi berdasarkan ketersediaan status dan kriteria tipe.
- `property total_dispatch` = Getter, untuk mengambil total dispatch operator.
- `total_dispatch.setter` = Setter, untuk mengubah nilai total dispatch dengan ketentuan tidak boleh negatif.

___________________________________________

### 3. Class `Misi`
Berfungsi untuk menyimpan data panggilan incident/misi yang masuk.

#### a. Class Attribute
- `total_panggilan_masuk` = Menyimpan jumlah seluruh objek misi yang dibuat.
- `tingkat_prioritas_default` = Menyimpan tingkat prioritas default ("High Alert").
- `batas_waktu_respon_detik` = Menyimpan batas waktu respon default.

#### b. Instance Attribute
- `id_misi` = Menyimpan ID unik misi.
- `nama_kejadian` = Menyimpan nama insiden/kejadian.
- `lokasi` = Menyimpan lokasi kejadian.
- `syarat_tipe` = Menyimpan daftar kriteria tipe hero yang dibutuhkan.
- `__reputasi_reward` = Menyimpan poin reward reputasi secara privat.

#### c. Method
- `__init__()` = Membuat objek misi dan menambahkan counter `total_panggilan_masuk`.
- `info_incident()` = Menampilkan informasi lengkap insiden/misi.
- `property reputasi_reward` = Getter, untuk mengambil poin reward reputasi.
- `reputasi_reward.setter` = Setter, untuk mengubah reward reputasi dengan ketentuan nilai harus lebih besar dari 0.


═════════════════════════════════════════════════════════════════════════════════════════════

## Panduan Menjalankan Program

### 1. Unduh File Program
Unduh file kode program Python yang telah dibuat.

### 2. Jalankan Program
Buka terminal, Command Prompt, atau editor seperti VS Code, lalu jalankan file tersebut.

### 3. Perhatikan Output Program
Program akan menampilkan beberapa bagian yang diujikan, yaitu:

1. Pembuatan dan penampil data hero (`tampilkan_stats()`).
2. Pengujian static method (`validasi_tipehero()`) dan class method (`reset_daftar()`).
3. Pembuatan dan penampil data misi (`info_incident()`).
4. Pembuatan data dispatcher dan penampil informasi (`info_operator()`).
5. Eksekusi proses dispatch tim hero (`dispatch_tim_hero()`).
6. Pemulihan status hero (`beristirahat()`).
7. Pengujian setter dengan data valid.
8. Pengujian setter dengan data tidak valid (Error handling `try-except`).


═════════════════════════════════════════════════════════════════════════════════════════════

## Panduan Pengujian

### Pengujian Program Utama
Seluruh pengujian class (`Hero`, `Misi`, `Dispatcher`), method, interaksi objek, serta enkapsulasi (setter valid & tidak valid) dapat dijalankan menggunakan satu blok kode berikut:

```python
 1. PENGUJIAN CLASS HERO
hero1 = Hero("Invisigal", "Intelligence", 85, "Standby", 90)
hero2 = Hero("Blonde Blazer", "Power", 90, "Standby", 95)
hero3 = Hero("Speedster", "Mobility", 75, "Standby", 85)

print(" 『 INSTANCE METHOD (TAMPILKAN STATS HERO) 』\n")
hero1.tampilkan_stats()
hero2.tampilkan_stats()
hero3.tampilkan_stats()

print("\n 『 STATIC METHOD (VALIDASI TIPE HERO) 』\n")
print(f" • Tipe 'Intelligence' -> {Hero.validasi_tipehero('Intelligence')}")
print(f" • Tipe 'Cybernetic'   -> {Hero.validasi_tipehero('Cybernetic')}")

print("\n 『 CLASS METHOD (RESET DAFTAR HERO) 』\n")
print(f" • Total hero sebelum reset: {Hero.total_hero}")
Hero.reset_daftar()
print(f" • Total hero setelah reset: {Hero.total_hero}")


 2. PENGUJIAN CLASS MISI
inc1 = Misi("INC-01", "Penyelidikan Villain", "Downtown", ["Intelligence", "Mobility"], 150)
inc2 = Misi("INC-02", "Kebakaran Gedung", "Sector 7", ["Power"], 80)

print("\n 『 INSTANCE METHOD (INFO INCIDENT) 』\n")
inc1.info_incident()
inc2.info_incident()


 3. PENGUJIAN CLASS DISPATCHER & INTERAKSI OBJEK
operator1 = Dispatcher("Player 1", "Night Shift", "Meja Utama 01", "PASS-1234")

print("\n 『 INSTANCE METHOD (INFO OPERATOR) 』\n")
operator1.info_operator()

print("\n 『 VERIFIKASI KODE AKSES 』\n")
print(f" • Password 'PASS-1234' -> {operator1.verifikasi_kode_akses('PASS-1234')}")
print(f" • Password 'PASS-SALAH' -> {operator1.verifikasi_kode_akses('PASS-SALAH')}")

print("\n 『 INSTANCE METHOD (DISPATCH TIM HERO) 』\n")
operator1.dispatch_tim_hero([hero1, hero3], inc1)

print("\nPerubahan Status:")
hero1.tampilkan_stats()
operator1.info_operator()

print("\n 『 INSTANCE METHOD (BERISTIRAHAT) 』\n")
hero1.beristirahat()
hero1.tampilkan_stats()


 4. PENGUJIAN SETTER DATA VALID
print("\n 『 PENGUJIAN SETTER (DATA VALID) 』\n")
print(f"Success rate awal {hero2.nama}: {hero2.persentase_sukses}%")
hero2.persentase_sukses = 98

print(f"Reward awal '{inc2.nama_kejadian}': {inc2.reputasi_reward} poin")
inc2.reputasi_reward = 120

print(f"Total dispatch awal {operator1.nama_operator}: {operator1.total_dispatch}")
operator1.total_dispatch = 5
print(f"Total dispatch baru: {operator1.total_dispatch}")


 5. PENGUJIAN SETTER DATA TIDAK VALID (EXCEPTION HANDLING)
print("\n 『 PENGUJIAN SETTER (DATA TIDAK VALID) 』\n")
try:
    print("[Uji 1] Mengisi persentase_sukses = 150...")
    hero2.persentase_sukses = 150
except ValueError as e:
    print(f"  [TERTANGKAP ERROR] {e}")

try:
    print("[Uji 2] Mengisi persentase_sukses = 'Sangat Tinggi'...")
    hero2.persentase_sukses = "Sangat Tinggi"
except ValueError as e:
    print(f"  [TERTANGKAP ERROR] {e}")

try:
    print("[Uji 3] Mengisi total_dispatch = -5...")
    operator1.total_dispatch = -5
except ValueError as e:
    print(f"  [TERTANGKAP ERROR] {e}")

try:
    print("[Uji 4] Mengisi reputasi_reward = 0...")
    inc2.reputasi_reward = 0
except ValueError as e:
    print(f"  [TERTANGKAP ERROR] {e}")