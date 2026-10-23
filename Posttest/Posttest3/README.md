# Sistem Dispatching dan Manajemen Alokasi Hero Pada Agensi Penugasan Pahlawan

Program aplikasi konsol berbasis Python untuk mengelola dan memproses pengiriman (*dispatch*) superhero pada sebuah agensi penugasan pahlawan. Program ini menerapkan prinsip Pemrograman Berbasis Objek (OOP) seperti Enkapsulasi, Properties, Inheritance, UML, serta penggunaan berbagai jenis Method.

===============================================================================================================================================

## Ringkasan Penjelasan Program

Program ini dibuat untuk mensimulasikan alur kerja operasional agensi hero. Sistem ini memiliki beberapa bagian utama:

1. **Manajemen Hero (`Hero`)**  
   Class `Hero` berperan sebagai superclass/parent class untuk jenis hero lain. Class ini menyimpan nama hero, status kesiapan hero (*Standby/Resting*), power level, dan persentase sukses.  
   Data penting seperti `persentase_sukses` disimpan secara private dan diakses melalui getter/setter.

2. **Spesialisasi Hero (Inheritance)**  
   Program memiliki beberapa subclass dari `Hero`, yaitu:
   - `HeroCombat`
   - `HeroIntelligence`
   - `HeroMobility`

   Setiap subclass memiliki atribut unik yang membedakannya dari parent class maupun subclass lainnya.

3. **Manajemen Operator (`Dispatcher`)**  
   Class `Dispatcher` mengelola operator yang bertugas mengirim tim hero ke sebuah misi. Dispatcher memeriksa jumlah hero, status kesiapan hero, dan kecocokan tipe hero dengan kebutuhan misi.

4. **Manajemen Misi (`Misi`)**  
   Class `Misi` menyimpan detail misi seperti ID misi, nama kejadian, lokasi, syarat tipe hero, reward reputasi, dan batas waktu respon.

5. **Manajemen Agensi (`Agency`)**  
   Class `Agency` digunakan untuk menampung daftar hero dan dispatcher. Relasi ini menunjukkan konsep agregasi.

6. **Pencatatan Dispatch (`DispatchLog`)**  
   Class `DispatchLog` digunakan untuk mencatat hasil dispatch, apakah sukses atau gagal. Log ini dibuat dan disimpan oleh `Dispatcher`.

===============================================================================================================================================

## Fitur Utama Program

Program menjalankan simulasi otomatis yang mencakup fitur-fitur berikut:

* **Pengelolaan Data Hero**
  - Membuat objek hero dari beberapa subclass.
  - Menampilkan data hero.
  - Menghitung total hero.
  - Mengubah maksimal jumlah hero dalam tim dispatch menggunakan `@classmethod`.
  - Memvalidasi tipe hero menggunakan `@staticmethod`.

* **Inheritance**
  - `Hero` sebagai superclass.
  - `HeroCombat`, `HeroIntelligence`, dan `HeroMobility` sebagai subclass.
  - Setiap subclass menggunakan `super().__init__(...)`.
  - Setiap subclass memiliki atribut unik.
  - Method `tampilkan_stats()` dioverride oleh setiap subclass.

* **Pengelolaan Misi**
  - Membuat data misi.
  - Menampilkan detail misi.
  - Menyimpan reward reputasi dengan validasi melalui setter.
  - Menyimpan batas waktu respon default sebesar 60 detik.

* **Pengelolaan Dispatcher**
  - Menampilkan info operator.
  - Verifikasi kode akses operator.
  - Menjalankan dispatch tim hero ke misi.
  - Menyimpan log hasil dispatch.

* **Manajemen Status Hero**
  - Hero yang selesai menjalankan misi berubah status menjadi `Resting`.
  - Hero dapat dipulihkan kembali menjadi `Standby` melalui method `beristirahat()`.

* **Validasi & Exception Handling**
  - Validasi `persentase_sukses`.
  - Validasi `total_dispatch`.
  - Validasi `reputasi_reward`.
  - Pengujian data valid dan tidak valid menggunakan `try-except`.

* **Pembersihan Terminal**
  - Program menggunakan fungsi `lanjut()` untuk menunggu input Enter dari user, lalu membersihkan terminal sebelum lanjut ke pengujian berikutnya.

------------------------------------------------------------------------------------------------------------------------------------------------

## Struktur Kode & Kelas

Program terdiri dari beberapa class utama dan pendukung:

### 1. `Hero`

Class `Hero` adalah superclass/parent class untuk seluruh jenis hero.

Atribut class:
- `total_hero`
- `nama_agency`
- `maksimal_tim_dispatch`

Atribut penting:
- `_nama` sebagai atribut protected.
- `_status` sebagai atribut protected.
- `__persentase_sukses` sebagai atribut private.
- `__id_hero` sebagai atribut private.

Method:
- `tampilkan_stats()`
- `beristirahat()`
- `ubah_maksimal_tim()` sebagai class method.
- `validasi_tipehero()` sebagai static method.

### 2. `HeroCombat`

Subclass dari `Hero`.

Atribut unik:
- `senjata`

Tipe hero:
- `Combat`

Method yang dioverride:
- `tampilkan_stats()`

### 3. `HeroIntelligence`

Subclass dari `Hero`.

Atribut unik:
- `gadget`

Tipe hero:
- `Intelligence`

Method yang dioverride:
- `tampilkan_stats()`

### 4. `HeroMobility`

Subclass dari `Hero`.

Atribut unik:
- `speed_level`

Tipe hero:
- `Mobility`

Method yang dioverride:
- `tampilkan_stats()`

### 5. `Dispatcher`

Class untuk operator yang mengelola proses dispatch.

Atribut penting:
- `nama_operator`
- `__kode_akses`
- `total_dispatch`
- `__logs`

Method:
- `verif_access()`
- `info_operator()`
- `dispatch_tim_hero()`
- `tampilkan_log()`

### 6. `DispatchLog`

Class untuk mencatat hasil dispatch.

Atribut:
- `nama_operator`
- `nama_misi`
- `sukses`

Method:
- `tampilkan()`

### 7. `Misi`

Class untuk menyimpan data misi.

Atribut class:
- `batas_waktu_respon_detik = 60`

Atribut instance:
- `id_misi`
- `nama_kejadian`
- `lokasi`
- `syarat_tipe`
- `reputasi_reward`

Method:
- `info_misi()`

### 8. `Agency`

Class untuk menampung daftar hero dan dispatcher.

Atribut:
- `nama`
- `daftar_hero`
- `daftar_dispatcher`

Method:
- `tambah_hero()`
- `tambah_dispatcher()`

------------------------------------------------------------------------------------------------------------------------------------------------

## Relasi UML yang Diterapkan

Program ini menerapkan tiga relasi UML yang diwajibkan, yaitu **asosiasi**, **agregasi**, dan **komposisi**.

### 1. Asosiasi

Relasi asosiasi terjadi ketika suatu class menggunakan objek dari class lain, tetapi tidak memilikinya secara permanen.

Pada program ini, asosiasi terjadi pada method:

```python
def dispatch_tim_hero(self, tim_hero, misi):
```

`Dispatcher` menggunakan objek `Hero` dan `Misi` sebagai parameter untuk memproses dispatch.

Contoh penggunaan:

```python
operator1.dispatch_tim_hero([hero1, hero3], inc1)
```

Artinya, `Dispatcher` menggunakan objek hero dan misi saat proses dispatch berlangsung.

### 2. Agregasi

Relasi agregasi terjadi ketika sebuah class menampung objek lain, tetapi objek tersebut tetap bisa hidup walaupun class penampungnya tidak ada.

Pada program ini, agregasi terjadi pada class `Agency`.

```python
class Agency:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_hero = []        
        self.daftar_dispatcher = []
```

Objek hero dan dispatcher dibuat di luar `Agency`, lalu dimasukkan ke daftar:

```python
agency.tambah_hero(hero1)
agency.tambah_dispatcher(operator1)
```

### 3. Komposisi

Relasi komposisi terjadi ketika suatu class membuat dan memiliki objek lain sebagai bagian dari dirinya.

Pada program ini, komposisi terjadi antara `Dispatcher` dan `DispatchLog`.

```python
self.__logs = []
```

Lalu objek `DispatchLog` dibuat di dalam class `Dispatcher`:

```python
self.__logs.append(DispatchLog(self.nama_operator, misi.nama_kejadian, True))
```

Artinya, log dispatch dibuat dan dimiliki oleh dispatcher.

------------------------------------------------------------------------------------------------------------------------------------------------

## Inheritance yang Diterapkan

Program menerapkan konsep inheritance dengan struktur berikut:

```text
Hero
├── HeroCombat
├── HeroIntelligence
└── HeroMobility
```

### Superclass

Superclass / parent class:

```python
class Hero:
```

### Subclass

Subclass / child class:

```python
class HeroCombat(Hero):
class HeroIntelligence(Hero):
class HeroMobility(Hero):
```

### Penggunaan `super()`

Setiap subclass memanggil constructor milik superclass menggunakan `super().__init__(...)`.

Contoh:

```python
class HeroCombat(Hero):
    def __init__(self, nama, power_level, persentase_sukses, senjata, status="Standby"):
        super().__init__(nama, power_level, persentase_sukses, status)
        self.senjata = senjata
```

### Atribut Tambahan Setiap Subclass

| Subclass | Atribut Unik |
|---|---|
| `HeroCombat` | `senjata` |
| `HeroIntelligence` | `gadget` |
| `HeroMobility` | `speed_level` |

### Method Overriding

Method `tampilkan_stats()` dari class `Hero` dioverride oleh setiap subclass.

Contoh pada `HeroCombat`:

```python
def tampilkan_stats(self):
    print(f"Hero: {self._nama} | Tipe: {self.tipe_hero} | Power: {self.power_level} | Senjata: {self.senjata} | SR: {self.persentase_sukses}% | Status: {self._status}")
```

### Protected dan Private

Protected attribute pada superclass:
```python
self._nama
self._status
```

Private attribute pada superclass:
```python
self.__persentase_sukses
self.__id_hero
```

Atribut protected digunakan oleh subclass, sedangkan atribut private digunakan untuk data yang harus dibatasi aksesnya.

------------------------------------------------------------------------------------------------------------------------------------------------

## Representasi Relasi UML Sederhana

```text
Hero <|-- HeroCombat
Hero <|-- HeroIntelligence
Hero <|-- HeroMobility

Dispatcher --> Hero : asosiasi
Dispatcher --> Misi : asosiasi

Agency o-- Hero : agregasi
Agency o-- Dispatcher : agregasi

Dispatcher *-- DispatchLog : komposisi
```

Keterangan:
- `<|--` menunjukkan inheritance.
- `-->` menunjukkan asosiasi.
- `o--` menunjukkan agregasi.
- `*--` menunjukkan komposisi.

------------------------------------------------------------------------------------------------------------------------------------------------

## Pengujian Program

Pengujian dilakukan langsung pada bagian *main code* dengan beberapa skenario berikut.

### 1. Pengujian Data Hero dan Inheritance

Menguji pembuatan objek hero dari subclass dan pemanggilan method `tampilkan_stats()`.

```python
hero1 = HeroIntelligence("Invisigal", 85, 90, "Smart Glasses")
hero2 = HeroCombat("Blonde Blazer", 90, 95, "Flame Sword")
hero3 = HeroMobility("Coupe", 75, 85, 10)

hero1.tampilkan_stats()
hero2.tampilkan_stats()
hero3.tampilkan_stats()
```

### 2. Pengujian Class Attribute, Static Method, dan Class Method

Menguji atribut class, static method, dan class method pada class `Hero`.

```python
print("Total Hero:", Hero.total_hero)
print("Nama Agency:", Hero.nama_agency)
print("Maksimal Tim:", Hero.maksimal_tim_dispatch)

print("Tipe Intelligence:", Hero.validasi_tipehero("Intelligence"))
print("Tipe Cybernetic:", Hero.validasi_tipehero("Cybernetic"))

print("Maksimal Tim sebelum:", Hero.maksimal_tim_dispatch)
Hero.ubah_maksimal_tim(4)
print("Maksimal Tim sesudah:", Hero.maksimal_tim_dispatch)
```

### 3. Pengujian Method Overriding

Setiap subclass memanggil method `tampilkan_stats()`, tetapi output yang ditampilkan berbeda karena masing-masing subclass memiliki atribut unik.

```python
hero1.tampilkan_stats()  # Menampilkan gadget
hero2.tampilkan_stats()  # Menampilkan senjata
hero3.tampilkan_stats()  # Menampilkan speed level
```

### 4. Pengujian Class `Misi`

Menguji pembuatan objek misi dan menampilkan detail misi.

```python
inc1 = Misi("INC-01", "Penyelidikan Villain", "Downtown", ["Intelligence", "Mobility"], 150)
inc2 = Misi("INC-02", "Kebakaran Gedung", "Sector 7", ["Combat"], 80)

inc1.info_misi()
inc2.info_misi()

print(f"Batas waktu respon: {Misi.batas_waktu_respon_detik} detik")
```

### 5. Pengujian Class `Dispatcher`

Menguji pembuatan operator dispatcher, menampilkan info operator, dan verifikasi kode akses.

```python
operator1 = Dispatcher("Player 1", "PASS-1234")
operator2 = Dispatcher("Player 2", "PASS-5678")

operator1.info_operator()
operator2.info_operator()

print(operator1.verif_access("PASS-1234"))
print(operator1.verif_access("SALAH"))
```

### 6. Pengujian Asosiasi

Menguji relasi asosiasi ketika `Dispatcher` menggunakan objek `Hero` dan `Misi` melalui parameter method.

```python
operator1.dispatch_tim_hero([hero1, hero3], inc1)
```

Pada contoh di atas:
- `operator1` adalah objek `Dispatcher`
- `[hero1, hero3]` adalah tim hero
- `inc1` adalah objek `Misi`

### 7. Pengujian Komposisi

Menguji log dispatch yang dibuat oleh class `Dispatcher`.

```python
operator1.tampilkan_log()
```

Log dibuat menggunakan class `DispatchLog` di dalam class `Dispatcher`.

### 8. Pengujian Agregasi

Menguji class `Agency` yang menampung daftar hero dan dispatcher.

```python
agency = Agency("Phoenix Agency")

agency.tambah_hero(hero1)
agency.tambah_hero(hero2)
agency.tambah_hero(hero3)

agency.tambah_dispatcher(operator1)
agency.tambah_dispatcher(operator2)

print("Jumlah Hero:", len(agency.daftar_hero))
print("Jumlah Dispatcher:", len(agency.daftar_dispatcher))
```

### 9. Pengujian Status Hero

Menguji perubahan status hero dari `Resting` kembali menjadi `Standby`.

```python
hero1.tampilkan_stats()
hero1.beristirahat()
hero1.tampilkan_stats()
```

### 10. Pengujian Setter dengan Data Valid

Menguji perubahan nilai atribut private melalui setter menggunakan data valid.

```python
hero2.persentase_sukses = 98
inc2.reputasi_reward = 120
```

### 11. Pengujian Setter dengan Data Tidak Valid

Menguji validasi setter menggunakan data yang tidak valid.

```python
try:
    hero2.persentase_sukses = 150
except ValueError as e:
    print("[ERROR]", e)

try:
    hero2.persentase_sukses = "Sangat Tinggi"
except ValueError as e:
    print("[ERROR]", e)

try:
    operator1.total_dispatch = -5
except ValueError as e:
    print("[ERROR]", e)

try:
    inc2.reputasi_reward = 0
except ValueError as e:
    print("[ERROR]", e)
```

------------------------------------------------------------------------------------------------------------------------------------------------

## Persyaratan Sistem

Untuk menjalankan program ini, pastikan sistem telah terinstal:

* **Python** versi 3.8 atau yang lebih baru.

------------------------------------------------------------------------------------------------------------------------------------------------

## Cara Menjalankan Program

1. Simpan kode program ke dalam file bernama:

```bash
posttets3_2509106066.py
```

2. Buka terminal atau Command Prompt (CMD).

3. Arahkan terminal ke folder tempat file `main.py` disimpan.

4. Jalankan program dengan perintah berikut:

```bash
python posttets3_2509106066.py
```

5. Saat program berjalan, tekan **Enter** untuk melanjutkan ke pengujian berikutnya. Terminal akan dibersihkan otomatis sebelum masuk ke bagian berikutnya.

------------------------------------------------------------------------------------------------------------------------------------------------