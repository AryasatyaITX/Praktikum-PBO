# Sistem Dispatching dan Manajemen Alokasi Hero Pada Agensi Penugasan Pahlawan

Program aplikasi konsol berbasis Python untuk mengelola dan memproses pengiriman (*dispatch*) superhero pada sebuah agensi penugasan pahlawan. Program ini menerapkan prinsip Pemrograman Berorientasi Objek (OOP) seperti Enkapsulasi, Properties, Inheritance, Relasi UML (Asosiasi, Agregasi, Komposisi), Abstraksi (Abstract Base Class), Polimorfisme, serta prinsip SOLID (DIP) dan beberapa jenis method.

===============================================================================================================================================

## Ringkasan Penjelasan Program

Program ini dibuat untuk mensimulasikan alur kerja operasional agensi hero. Sistem ini memiliki beberapa bagian utama:

1. **Manajemen Hero (`Hero`)**
   Class `Hero` adalah *abstract class* sekaligus superclass untuk jenis hero lain. Class ini menyimpan nama hero, status kesiapan hero (*Standby/Resting*), power level, dan persentase sukses.
   Data penting seperti `persentase_sukses` disimpan secara private dan diakses melalui getter/setter.

2. **Spesialisasi Hero (Inheritance)**
   Program memiliki beberapa subclass dari `Hero`, yaitu:
   - `HeroCombat`
   - `HeroIntelligence`
   - `HeroMobility`
   - `HeroVigor`

   Setiap subclass memiliki atribut unik yang membedakannya dari parent class maupun subclass lainnya.

3. **Manajemen Operator (`Dispatcher`)**
   Class `Dispatcher` mengelola operator yang bertugas mengirim tim hero ke sebuah misi. Dispatcher memeriksa jumlah hero, status kesiapan hero, lalu meminta sebuah penilai (`MissionEvaluator`) untuk menilai apakah tim layak menjalankan misi.

4. **Penilaian Misi (`MissionEvaluator`)**
   Abstract class dengan dua penilai konkret, yaitu `TypeEvaluator` (menilai kecocokan tipe hero) dan `SuccessRateEvaluator` (menilai rata-rata persentase sukses tim).

5. **Manajemen Misi (`Misi`)**
   Class `Misi` menyimpan detail misi seperti ID misi, nama kejadian, lokasi, syarat tipe hero, reward reputasi, dan batas waktu respon.

6. **Manajemen Agensi (`Agency`)**
   Class `Agency` digunakan untuk menampung daftar hero dan dispatcher. Relasi ini menunjukkan konsep agregasi.

7. **Pencatatan Dispatch (`DispatchLog`)**
   Class `DispatchLog` digunakan untuk mencatat hasil dispatch, apakah sukses atau gagal. Log ini dibuat dan disimpan oleh `Dispatcher`.

8. **Panggilan Darurat (`Competingcalls`, `Hackcalls`)**
   Dua jenis panggilan yang tidak berhubungan lewat pewarisan tetapi sama-sama memiliki method `tangani()`, dipakai untuk contoh duck typing.

===============================================================================================================================================

## Fitur Utama Program

Program menjalankan simulasi otomatis yang mencakup fitur-fitur berikut:

* **Pengelolaan Data Hero**
  - Membuat objek hero dari beberapa subclass.
  - Menampilkan data hero.
  - Menghitung total hero.
  - Mengubah maksimal jumlah hero dalam tim dispatch menggunakan `@classmethod`.
  - Memvalidasi tipe hero menggunakan `@staticmethod`.

* **Inheritance, Abstraksi, dan Polimorfisme**
  - `Hero` sebagai abstract class dengan 2 abstract method.
  - `HeroCombat`, `HeroIntelligence`, `HeroMobility`, dan `HeroVigor` sebagai subclass yang mengimplementasikan seluruh abstract method.
  - Method `tampilkan_stats()` dan `aksi_khusus()` dioverride oleh setiap subclass.
  - Duck typing pada `Competingcalls` dan `Hackcalls`.
  - Operator overloading `__lt__` dan `__str__`.

* **Pengelolaan Misi**
  - Membuat data misi.
  - Menampilkan detail misi.
  - Menyimpan reward reputasi dengan validasi melalui setter.
  - Menyimpan batas waktu respon default sebesar 60 detik.

* **Pengelolaan Dispatcher**
  - Menampilkan info operator.
  - Verifikasi kode akses operator.
  - Menjalankan dispatch tim hero ke misi dengan penilai yang dapat diganti (DIP).
  - Menyimpan log hasil dispatch.

* **Manajemen Status Hero**
  - Hero yang selesai menjalankan misi berubah status menjadi `Resting`.
  - Hero dapat dipulihkan kembali menjadi `Standby` melalui method `beristirahat()`.

* **Validasi & Exception Handling**
  - Validasi `persentase_sukses`.
  - Validasi `total_dispatch`.
  - Validasi `reputasi_reward`.
  - Setter `status` pada `Hero` serta property read-only `nama`, `tipe_hero`, dan `id_hero`.
  - Pengujian data valid dan tidak valid menggunakan `try-except`.

* **Pembersihan Terminal**
  - Program menggunakan fungsi `lanjut()` untuk menunggu input Enter dari user, lalu membersihkan terminal sebelum lanjut ke pengujian berikutnya.

------------------------------------------------------------------------------------------------------------------------------------------------

## Struktur Code & Class

Program terdiri dari dua file: `posttest3_2509106066_AryasatyaRakhaPhanyputa.py` (definisi kelas) dan `main.py` (pengujian). Setiap kelas dijelaskan dengan pola tabel yang sama: atribut kelas, atribut instance, property, dan method.

### Ringkasan Seluruh Kelas

| No | Class  | Jenis | Induk | Peran |
|---|---|---|---|---|
| 1 | `Hero` | Abstract class (`ABC`) | - | Superclass seluruh hero |
| 2 | `HeroCombat` | Subclass | `Hero` | Hero tipe Combat |
| 3 | `HeroIntelligence` | Subclass | `Hero` | Hero tipe Intelligence |
| 4 | `HeroMobility` | Subclass | `Hero` | Hero tipe Mobility |
| 5 | `HeroVigor` | Subclass | `Hero` | Hero tipe Vigor |
| 6 | `MissionEvaluator` | Abstract class (`ABC`) | - | Abstraksi penilai misi (DIP) |
| 7 | `TypeEvaluator` | Subclass | `MissionEvaluator` | Penilai berdasarkan kecocokan tipe hero |
| 8 | `SuccessRateEvaluator` | Subclass | `MissionEvaluator` | Penilai berdasarkan rata-rata persentase sukses |
| 9 | `DispatchLog` | Class biasa | - | Pencatat hasil dispatch (komposisi) |
| 10 | `Dispatcher` | Class biasa | - | Operator yang mengirim tim hero |
| 11 | `Misi` | Class biasa | - | Data misi |
| 12 | `Agency` | Class biasa | - | Penampung hero dan dispatcher (agregasi) |
| 13 | `Competingcalls`, `Hackcalls` | Class biasa | - | Contoh duck typing |
| 14 | `proses_panggilan()` | Fungsi | - | Memanggil `tangani()` pada objek apa pun |

### 1. Class `Hero` (Abstract Base Class)

Superclass abstrak untuk semua hero. Objeknya tidak bisa dibuat langsung, hanya lewat subclass.

**Atribut kelas**

| Atribut | Nilai awal | Fungsi |
|---|---|---|
| `total_hero` | `0` | Penghitung jumlah hero yang dibuat, juga dipakai sebagai ID hero |
| `nama_agency` | `"Phoenix Agency"` | Nama agensi |
| `maksimal_tim_dispatch` | `3` | Batas jumlah hero dalam satu tim dispatch |

**Atribut instance**

| Atribut | Akses | Keterangan |
|---|---|---|
| `_nama` | Protected | Diakses lewat property `nama`, boleh dipakai subclass |
| `_status` | Protected | Diakses lewat property `status`, bernilai `Standby` atau `Resting` |
| `power_level` | Public | Tingkat kekuatan hero, dipakai oleh `__lt__` |
| `__persentase_sukses` | Private | Diakses lewat property `persentase_sukses` |
| `__id_hero` | Private | Diakses lewat property `id_hero` |

**Property**

| Property | Jenis | Validasi di setter |
|---|---|---|
| `nama` | Getter saja | - (read-only) |
| `status` | Getter dan setter | Tanpa validasi, dipakai `Dispatcher` untuk mengubah status |
| `persentase_sukses` | Getter dan setter | Harus angka (`int` atau `float`) dan berada di rentang 0 - 100 |
| `tipe_hero` | Getter saja | - (membaca konstanta `TIPE` milik subclass) |
| `id_hero` | Getter saja | - (read-only) |

**Method**

| Method | Jenis | Fungsi |
|---|---|---|
| `info_dasar()` | Method konkret | Menyusun teks data dasar hero, dipakai bersama oleh semua subclass |
| `beristirahat()` | Method konkret | Mengubah status `Resting` menjadi `Standby` |
| `ubah_maksimal_tim()` | Class method | Mengubah `maksimal_tim_dispatch` (harus lebih dari 0) |
| `validasi_tipehero()` | Static method | Mengecek apakah tipe hero termasuk tipe yang valid |
| `tampilkan_stats()` | Abstract method 1 | Menampilkan data hero, ditentukan tiap subclass |
| `aksi_khusus()` | Abstract method 2 | Aksi khusus hero, ditentukan tiap subclass |
| `__lt__()` | Magic method | Operator overloading, membandingkan hero berdasarkan `power_level` |

### 2. Subclass `Hero`

Empat subclass yang masing-masing menambah satu atribut unik. Semuanya memanggil `super().__init__(...)`, memiliki konstanta `TIPE`, dan mengimplementasikan seluruh abstract method.

**Atribut tambahan**

| Subclass | Konstanta `TIPE` | Atribut unik | Akses |
|---|---|---|---|
| `HeroCombat` | `"Combat"` | `senjata` | Public |
| `HeroIntelligence` | `"Intelligence"` | `gadget` | Public |
| `HeroMobility` | `"Mobility"` | `speed_level` | Public |
| `HeroVigor` | `"Vigor"` | `stamina` | Public |

**Method yang dioverride**

| Subclass | `tampilkan_stats()` | `aksi_khusus()` |
|---|---|---|
| `HeroCombat` | Data dasar + `senjata` | Menyerang menggunakan `senjata` |
| `HeroIntelligence` | Data dasar + `gadget` | Menganalisis situasi dengan `gadget` |
| `HeroMobility` | Data dasar + `speed_level` | Bergerak cepat sesuai `speed_level` |
| `HeroVigor` | Data dasar + `stamina` | Menampilkan besar `stamina` |

### 3. Class `MissionEvaluator` (Abstract Base Class) beserta Subclass

Abstraksi penilai misi. `Dispatcher` bergantung pada kelas ini, bukan pada penilai konkret (DIP).

**Method**

| Kelas | Jenis | Method | Fungsi |
|---|---|---|---|
| `MissionEvaluator` | Abstract class | `nilai(tim, misi)` (abstract) | Kontrak untuk semua penilai |
| `TypeEvaluator` | Subclass | `nilai(tim, misi)` | Tim lolos jika memiliki setiap tipe hero yang disyaratkan misi |
| `SuccessRateEvaluator` | Subclass | `nilai(tim, misi)` | Tim lolos jika rata-rata persentase sukses mencapai batas |

**Atribut `SuccessRateEvaluator`**

| Atribut | Akses | Keterangan |
|---|---|---|
| `batas` | Public | Batas dasar persentase sukses (default `90`). Batas yang dibutuhkan = `batas + reputasi_reward // 50`, maksimal 100 |

### 4. Class `Dispatcher`

Operator yang mengirim tim hero ke misi dan menyimpan log hasilnya.

**Atribut instance**

| Atribut | Akses | Keterangan |
|---|---|---|
| `nama_operator` | Public | Nama operator |
| `__kode_akses` | Private | Hanya bisa dicek lewat `verif_access()` |
| `__total_dispatch` | Private | Diakses lewat property `total_dispatch` |
| `__logs` | Private | Daftar `DispatchLog` milik dispatcher (komposisi) |
| `penilai` | Public | Objek `MissionEvaluator`, default `TypeEvaluator` (DIP) |

**Property**

| Property | Validasi di setter |
|---|---|
| `total_dispatch` | Tidak boleh negatif |

**Method**

| Method | Jenis | Fungsi |
|---|---|---|
| `verif_access()` | Method biasa | Membandingkan input dengan kode akses |
| `info_operator()` | Method biasa | Menampilkan info operator, kode akses ditampilkan sebagai `[PRIVATE]` |
| `dispatch_tim_hero()` | Method biasa (asosiasi) | Memproses pengiriman tim hero ke sebuah misi |
| `tampilkan_log()` | Method biasa | Mencetak seluruh log milik operator memakai `__str__` |

**Alur `dispatch_tim_hero()`**

| Langkah | Pemeriksaan | Jika tidak terpenuhi |
|---|---|---|
| 1 | Jumlah hero antara 1 dan `maksimal_tim_dispatch` | Gagal, dicatat di log |
| 2 | Semua hero berstatus `Standby` | Gagal, dicatat di log |
| 3 | `penilai.nilai(tim_hero, misi)` bernilai `True` | Misi gagal, hero menjadi `Resting`, dicatat di log |
| 4 | Semua syarat terpenuhi | `total_dispatch` bertambah, hero menjadi `Resting`, log sukses dicatat |

### 5. Class `DispatchLog`

Pencatat hasil dispatch. Dibuat dan dimiliki oleh `Dispatcher`.

**Atribut instance**

| Atribut | Akses | Keterangan |
|---|---|---|
| `nama_operator` | Public | Operator yang memproses |
| `nama_misi` | Public | Misi yang diproses |
| `sukses` | Public | `True` jika misi sukses |

**Method**

| Method | Jenis | Fungsi |
|---|---|---|
| `__str__()` | Magic method | Operator overloading, menentukan tampilan log saat di-`print()` |

### 6. Class `Misi`

Menyimpan data misi.

**Atribut kelas**

| Atribut | Nilai awal | Fungsi |
|---|---|---|
| `batas_waktu_respon_detik` | `60` | Batas waktu respon misi dalam detik |

**Atribut instance**

| Atribut | Akses | Keterangan |
|---|---|---|
| `id_misi` | Public | ID misi |
| `nama_kejadian` | Public | Nama kejadian |
| `lokasi` | Public | Lokasi kejadian |
| `syarat_tipe` | Public | Daftar tipe hero yang dibutuhkan |
| `__reputasi_reward` | Private | Diakses lewat property `reputasi_reward` |

**Property**

| Property | Validasi di setter |
|---|---|
| `reputasi_reward` | Harus lebih dari 0 |

**Method**

| Method | Jenis | Fungsi |
|---|---|---|
| `info_misi()` | Method biasa | Menampilkan detail misi |

### 7. Class `Agency`

Menampung hero dan dispatcher yang dibuat di luar (agregasi).

**Atribut instance**

| Atribut | Akses | Keterangan |
|---|---|---|
| `nama` | Public | Nama agensi |
| `daftar_hero` | Public | List objek `Hero` |
| `daftar_dispatcher` | Public | List objek `Dispatcher` |

**Method**

| Method | Jenis | Fungsi |
|---|---|---|
| `tambah_hero()` | Method biasa | Menambahkan hero ke agensi |
| `tambah_dispatcher()` | Method biasa | Menambahkan dispatcher ke agensi |

### 8. Class `Competingcalls`, `Hackcalls`, dan Fungsi `proses_panggilan()`

Dua kelas yang tidak berhubungan lewat pewarisan, tetapi sama-sama memiliki method `tangani()` (duck typing).

**Atribut instance**

| Kelas | Atribut | Keterangan |
|---|---|---|
| `Competingcalls` | `opsi_a`, `opsi_b` | Dua pilihan yang harus dipilih salah satu |
| `Hackcalls` | `target` | Target yang diretas operator |

**Method dan fungsi**

| Nama | Jenis | Fungsi |
|---|---|---|
| `Competingcalls.tangani()` | Method biasa | Meminta pemain memilih salah satu opsi |
| `Hackcalls.tangani()` | Method biasa | Meretas target tanpa mengirim hero |
| `proses_panggilan()` | Fungsi | Memanggil `panggilan.tangani()` pada objek apa pun |

### 9. Struktur `main.py`

| Bagian | Fungsi |
|---|---|
| `lanjut()` | Menunggu Enter lalu membersihkan terminal |
| Data Hero | Membuat 4 hero (`hero1` - `hero4`) dan menguji class attribute, static method, class method |
| Abstract Class, Polimorfisme, Duck Typing, Operator Overloading | Menguji konsep abstraksi sampai `__lt__` |
| Data Misi dan Dispatcher | Membuat `inc1`, `inc2`, `operator1`, `operator2` |
| Asosiasi, DIP, Komposisi, Agregasi | Menguji relasi antar kelas dan dependency injection |
| Status Hero dan Setter | Menguji `beristirahat()` serta setter valid dan tidak valid |

------------------------------------------------------------------------------------------------------------------------------------------------

## Class Diagram dan Relasi UML

Diagram berikut menampilkan tiga relasi UML yang diwajibkan, yaitu **asosiasi**, **agregasi**, dan **komposisi**.

![Class Diagram](Images/UML.drawio.png)

Keterangan simbol:
- Garis putus-putus dengan panah (`..>`) menunjukkan asosiasi.
- Garis dengan belah ketupat kosong di sisi induk (`o--`) menunjukkan agregasi.
- Garis dengan belah ketupat hitam di sisi induk (`*--`) menunjukkan komposisi.

Ketiga relasi di bawah ini benar-benar ada di kode program.

### 1. Asosiasi: `Dispatcher` ke `Hero` dan `Dispatcher` ke `Misi`

`Dispatcher` hanya menggunakan objek `Hero` dan `Misi` sebagai parameter method `dispatch_tim_hero()`, tanpa menyimpannya sebagai atribut tetap. Karena itu hubungannya longgar: hero dan misi hidup mandiri dan hanya dipakai sementara saat dispatch berlangsung.

```python
def dispatch_tim_hero(self, tim_hero, misi):
```

```python
operator1.dispatch_tim_hero([hero1, hero3], inc1)
```

### 2. Agregasi: `Agency` ke `Hero` dan `Agency` ke `Dispatcher`

`Agency` menampung daftar hero dan dispatcher yang dibuat di luar, lalu dimasukkan lewat `tambah_hero()` dan `tambah_dispatcher()`. Jenis relasinya agregasi, bukan komposisi, karena hero dan dispatcher tetap bisa hidup mandiri walaupun `Agency` dihapus: mereka tidak dibuat oleh `Agency` dan dapat berpindah ke agency lain.

```python
class Agency:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_hero = []
        self.daftar_dispatcher = []
```

```python
agency.tambah_hero(hero1)
agency.tambah_dispatcher(operator1)
```

### 3. Komposisi: `Dispatcher` ke `DispatchLog`

`DispatchLog` dibuat langsung di dalam `Dispatcher` (pada method `dispatch_tim_hero()`) dan disimpan di atribut private `__logs`. Jenis relasinya komposisi, bukan agregasi, karena log tidak dibuat di luar, tidak dipakai bersama objek lain, dan tidak bermakna tanpa dispatcher yang mencatatnya. Jika `Dispatcher` dihapus, log miliknya ikut hilang.

```python
self.__logs = []
```

```python
self.__logs.append(DispatchLog(self.nama_operator, misi.nama_kejadian, True))
```

### Ringkasan perbedaan agregasi dan komposisi

| Aspek | Agregasi (`Agency`) | Komposisi (`Dispatcher` dan `DispatchLog`) |
|---|---|---|
| Lokasi pembuatan objek bagian | Di luar, lalu dikirim ke penampung | Langsung di dalam objek induk |
| Bentuk kepemilikan | Referensi bebas | Eksklusif milik satu induk |
| Dapat hidup mandiri | Ya | Tidak |
| Saat induk dihapus | Hero dan dispatcher tetap ada | Log ikut musnah |

------------------------------------------------------------------------------------------------------------------------------------------------

## Inheritance yang Diterapkan

Program menerapkan konsep inheritance dengan struktur berikut:

```text
Hero (abstract)
├── HeroCombat
├── HeroIntelligence
├── HeroMobility
└── HeroVigor
```

### Superclass

Superclass / parent class:

```python
class Hero(ABC):
```

### Subclass

Subclass / child class:

```python
class HeroCombat(Hero):
class HeroIntelligence(Hero):
class HeroMobility(Hero):
class HeroVigor(Hero):
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
| `HeroVigor` | `stamina` |

### Method Overriding

Method `tampilkan_stats()` dan `aksi_khusus()` dari class `Hero` dioverride oleh setiap subclass.

Contoh pada `HeroCombat`:

```python
def tampilkan_stats(self):
    print(self.info_dasar() + f" | Senjata: {self.senjata}")

def aksi_khusus(self):
    print(f"{self.nama} menyerang menggunakan {self.senjata}!")
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

| Atribut | Visibilitas | Akses dari luar |
|---|---|---|
| `_nama` | Protected | Property `nama` (read-only) |
| `_status` | Protected | Property `status` (getter dan setter) |
| `__persentase_sukses` | Private | Property `persentase_sukses` (setter dengan validasi) |
| `__id_hero` | Private | Property `id_hero` (read-only) |

------------------------------------------------------------------------------------------------------------------------------------------------

## Abstraksi (Abstract Base Class)

Abstraksi diterapkan dengan modul `abc` (`ABC` dan `@abstractmethod`). Abstract class berfungsi sebagai kontrak yang memaksa kelas anak mengimplementasikan method tertentu. Jika ada method yang belum diimplementasikan, error langsung muncul saat objek dibuat, bukan saat method dipanggil.

### Abstract class `Hero`

```python
class Hero(ABC):
    ...
    @abstractmethod
    def tampilkan_stats(self):
        pass

    @abstractmethod
    def aksi_khusus(self):
        pass
```

`Hero` memiliki 2 abstract method, yaitu `tampilkan_stats()` dan `aksi_khusus()`.

### Subclass yang mengimplementasikan seluruh abstract method

| Subclass | `tampilkan_stats()` | `aksi_khusus()` |
|---|---|---|
| `HeroCombat` | menampilkan data + `senjata` | menyerang menggunakan senjata |
| `HeroIntelligence` | menampilkan data + `gadget` | menganalisis situasi dengan gadget |
| `HeroMobility` | menampilkan data + `speed_level` | bergerak cepat sesuai `speed_level` |
| `HeroVigor` | menampilkan data + `stamina` | menampilkan besar `stamina` |

Keempat subclass tetap memakai `super().__init__(...)`, memiliki atribut unik masing-masing, serta memakai atribut protected (`_nama`, `_status`) dan private (`__persentase_sukses`, `__id_hero`) dari `Hero`.

### Method konkret yang dipakai bersama

`Hero` juga memiliki method biasa (konkret) yang diwarisi dan dipakai oleh semua subclass:

- `info_dasar()` menyusun teks data dasar hero. Dipanggil di dalam `tampilkan_stats()` milik setiap subclass.
- `beristirahat()` mengembalikan status hero dari `Resting` ke `Standby`.

Pola ini sama seperti `jalankan()` pada materi: alur umum ditulis sekali di abstract class, sedangkan bagian yang berbeda diserahkan ke subclass.

### Bukti abstract class tidak dapat diinstansiasi

```python
try:
    Bunny = Hero("Bunny", 1, 50)
except TypeError as e:
    print("[Bukti ABSTRAKSI] Tidak bisa instansiasi Hero:", e)
```

Output:

```text
[Bukti ABSTRAKSI] Tidak bisa instansiasi Hero: Can't instantiate abstract class Hero without an implementation for abstract methods 'aksi_khusus', 'tampilkan_stats'
```

Error `TypeError` muncul saat `Hero(...)` dipanggil, sebelum ada data yang diproses.

Abstract class kedua adalah `MissionEvaluator` (method abstrak `nilai()`), yang diimplementasikan oleh `TypeEvaluator` dan `SuccessRateEvaluator`. Pemakaiannya dijelaskan di bagian SOLID.

------------------------------------------------------------------------------------------------------------------------------------------------

## Polimorfisme

Polimorfisme berarti satu interface dengan banyak implementasi: kode yang sama dapat bekerja dengan objek bertipe berbeda selama objek tersebut memiliki method yang diharapkan.

### 1. Polimorfisme via pewarisan (method overriding)

Method `aksi_khusus()` dan `tampilkan_stats()` di-override oleh `HeroCombat`, `HeroIntelligence`, `HeroMobility`, dan `HeroVigor` dengan perilaku berbeda. Pemanggilannya lewat satu loop yang berisi objek dari subclass berbeda:

```python
for hero in [hero1, hero2, hero3, hero4]:
    hero.aksi_khusus()
```

Output:

```text
Invisigal menganalisis situasi dengan gadget Smart Glasses!
Blonde Blazer menyerang menggunakan Necklace Power!
Coupe bergerak cepat dengan speed level 10!
Golem mempunyai stamina sebesar 98!
```

Loop tidak perlu tahu tipe hero. Python memilih implementasi yang sesuai saat program berjalan (*dynamic dispatch*).

### 2. Duck typing

`Competingcalls` dan `Hackcalls` tidak berhubungan lewat pewarisan, tetapi keduanya memiliki method `tangani()`. Keduanya dipanggil lewat satu fungsi yang sama:

```python
def proses_panggilan(panggilan):
    panggilan.tangani()

proses_panggilan(Competingcalls("Selamatkan bank", "Selamatkan sekolah. Jika tidak memilih maka opsi tersebut akan menghilang!"))
proses_panggilan(Hackcalls("sistem keamanan gedung"))
```

Output:

```text
Pilih satu: 'Selamatkan bank' atau 'Selamatkan sekolah. Jika tidak memilih maka opsi tersebut akan menghilang!'.
[HACKING] Tidak ada hero dikirim atau membantu hero, operator meretas sistem keamanan gedung.
```

`proses_panggilan()` hanya membutuhkan objek yang memiliki `tangani()`, tanpa peduli kelas atau pewarisannya.

### 3. Operator overloading

| Magic method | Kelas | Fungsi |
|---|---|---|
| `__lt__` | `Hero` | Membandingkan hero berdasarkan `power_level`, sehingga operator `<` dan fungsi `max()` dapat dipakai pada objek hero |
| `__str__` | `DispatchLog` | Menentukan tampilan log saat objek di-`print()` |

```python
print(f"{hero1.nama} ({hero1.power_level}) < {hero2.nama} ({hero2.power_level}) ? {hero1 < hero2}")
print(f"{hero2.nama} ({hero2.power_level}) < {hero3.nama} ({hero3.power_level}) ? {hero2 < hero3}")
print("Hero terkuat (max):", max(hero1, hero2, hero3).nama)
```

Output:

```text
Invisigal (85) < Blonde Blazer (90) ? True
Blonde Blazer (90) < Coupe (75) ? False
Hero terkuat (max): Blonde Blazer
```

Contoh `__str__` pada log dispatch:

```text
[LOG] SUKSES | Operator: Player 1 | Misi: Penyelidikan Villain
[LOG] GAGAL | Operator: Player 1 | Misi: Penyelidikan Villain
```

------------------------------------------------------------------------------------------------------------------------------------------------

## Penerapan Prinsip SOLID

Program menerapkan satu prinsip SOLID, yaitu **DIP**, dan penerapannya benar-benar ada di kode. Prinsip lain tidak diklaim.

### DIP (Dependency Inversion Principle)

Kelas tingkat tinggi `Dispatcher` bergantung pada abstraksi `MissionEvaluator`, bukan pada kelas penilai tertentu. Objek penilai dikirim dari luar lewat constructor (*dependency injection*):

```python
class MissionEvaluator(ABC):
    @abstractmethod
    def nilai(self, tim, misi):
        pass

class Dispatcher:
    def __init__(self, nama_operator, kode_akses, penilai: MissionEvaluator = None):
        ...
        self.penilai = penilai if penilai is not None else TypeEvaluator()
```

`Dispatcher` memanggil `self.penilai.nilai(tim_hero, misi)` tanpa tahu jenis penilainya. Jika `penilai` tidak diberikan, `TypeEvaluator` dipakai sebagai nilai default agar `Dispatcher` tetap mudah dibuat. Pengujiannya di `main.py`:

```python
operator1 = Dispatcher("Player 1", "PASS-1234")                                       # default: TypeEvaluator
operator2 = Dispatcher("Player 2", "PASS-5678", penilai=SuccessRateEvaluator(90))     # disuntikkan dari luar
```

Output, misi yang sama dengan hero yang sama dinilai berbeda oleh dua `Dispatcher` yang kodenya tidak diubah:

```text
Operator 1 (TypeEvaluator, default):
[DISPATCH] Player 1 memproses 'Penyelidikan Villain'...
TypeEvaluator memeriksa tipe tim ['Combat'] terhadap syarat misi ['Intelligence', 'Mobility']
[MISI GAGAL] Tim tidak memenuhi penilaian misi.
...
Operator 2 (SuccessRateEvaluator, batas 90%):
[DISPATCH] Player 2 memproses 'Penyelidikan Villain'...
SuccessRateEvaluator: rata-rata tim 95.0%, dibutuhkan 93%
[MISI SUKSES] Tim berhasil!
```

### Ringkasan

| Prinsip | Penerapan di program |
|---|---|
| DIP | `Dispatcher` menerima `penilai: MissionEvaluator` dari luar lewat constructor, tidak membuat penilai konkret sendiri secara permanen |

------------------------------------------------------------------------------------------------------------------------------------------------

## Pengujian Program

Pengujian dilakukan langsung pada bagian *main code* dengan beberapa skenario berikut.

### 1. Pengujian Data Hero dan Inheritance

Menguji pembuatan objek hero dari subclass dan pemanggilan method `tampilkan_stats()`.

```python
hero1 = HeroIntelligence("Invisigal", 85, 90, "Smart Glasses")
hero2 = HeroCombat("Blonde Blazer", 90, 95, "Necklace Power")
hero3 = HeroMobility("Coupe", 75, 85, 10)
hero4 = HeroVigor("Golem", 90, 60, 98)

hero1.tampilkan_stats()
hero2.tampilkan_stats()
hero3.tampilkan_stats()
hero4.tampilkan_stats()
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

### 3. Pengujian Abstract Class

Membuat objek `Hero` langsung harus gagal dengan `TypeError`.

```python
try:
    Bunny = Hero("Bunny", 1, 50)
except TypeError as e:
    print("[Bukti ABSTRAKSI] Tidak bisa instansiasi Hero:", e)
```

### 4. Pengujian Polimorfisme (Override)

Setiap subclass memanggil `aksi_khusus()` lewat satu loop, tetapi output yang ditampilkan berbeda.

```python
for hero in [hero1, hero2, hero3, hero4]:
    hero.aksi_khusus()
```

### 5. Pengujian Duck Typing

```python
proses_panggilan(Competingcalls("Selamatkan bank", "Selamatkan sekolah. Jika tidak memilih maka opsi tersebut akan menghilang!"))
proses_panggilan(Hackcalls("sistem keamanan gedung"))
```

### 6. Pengujian Operator Overloading

```python
print(f"{hero1.nama} ({hero1.power_level}) < {hero2.nama} ({hero2.power_level}) ? {hero1 < hero2}")
print(f"{hero2.nama} ({hero2.power_level}) < {hero3.nama} ({hero3.power_level}) ? {hero2 < hero3}")
print("Hero terkuat (max):", max(hero1, hero2, hero3).nama)
operator1.tampilkan_log()   # memakai __str__ pada DispatchLog
```

### 7. Pengujian Class `Misi`

Menguji pembuatan objek misi dan menampilkan detail misi.

```python
inc1 = Misi("INC-01", "Penyelidikan Villain", "Downtown", ["Intelligence", "Mobility"], 150)
inc2 = Misi("INC-02", "Kebakaran Gedung", "Sector 7", ["Combat"], 80)

inc1.info_misi()
inc2.info_misi()

print(f"Batas waktu respon: {Misi.batas_waktu_respon_detik} detik")
```

### 8. Pengujian Class `Dispatcher`

Menguji pembuatan operator dispatcher (dengan penilai default dan penilai yang disuntikkan), menampilkan info operator, dan verifikasi kode akses.

```python
operator1 = Dispatcher("Player 1", "PASS-1234")
operator2 = Dispatcher("Player 2", "PASS-5678", penilai=SuccessRateEvaluator(90))

operator1.info_operator()
operator2.info_operator()

print(operator1.verif_access("PASS-1234"))
print(operator1.verif_access("SALAH"))
```

### 9. Pengujian Asosiasi

Menguji relasi asosiasi ketika `Dispatcher` menggunakan objek `Hero` dan `Misi` melalui parameter method.

```python
operator1.dispatch_tim_hero([hero1, hero3], inc1)
```

Pada contoh di atas:
- `operator1` adalah objek `Dispatcher`
- `[hero1, hero3]` adalah tim hero
- `inc1` adalah objek `Misi`

### 10. Pengujian DIP (Dependency Inversion)

Misi yang sama dinilai oleh dua `Dispatcher` dengan penilai berbeda, tanpa mengubah kelas `Dispatcher`.

```python
operator1.dispatch_tim_hero([hero2], inc1)   # TypeEvaluator: gagal
hero2.beristirahat()
operator2.dispatch_tim_hero([hero2], inc1)   # SuccessRateEvaluator: sukses
```

### 11. Pengujian Komposisi

Menguji log dispatch yang dibuat oleh class `Dispatcher`.

```python
operator1.tampilkan_log()
```

Log dibuat menggunakan class `DispatchLog` di dalam class `Dispatcher`.

### 12. Pengujian Agregasi

Menguji class `Agency` yang menampung daftar hero dan dispatcher.

```python
agency = Agency("Phoenix Agency")

agency.tambah_hero(hero1)
agency.tambah_hero(hero2)
agency.tambah_hero(hero3)
agency.tambah_hero(hero4)

agency.tambah_dispatcher(operator1)
agency.tambah_dispatcher(operator2)

print("Jumlah Hero:", len(agency.daftar_hero))
print("Jumlah Dispatcher:", len(agency.daftar_dispatcher))
```

### 13. Pengujian Status Hero

Menguji perubahan status hero dari `Resting` kembali menjadi `Standby`.

```python
hero1.tampilkan_stats()
hero1.beristirahat()
hero1.tampilkan_stats()
```

### 14. Pengujian Setter dengan Data Valid

Menguji perubahan nilai atribut private melalui setter menggunakan data valid.

```python
hero2.persentase_sukses = 98
inc2.reputasi_reward = 120
```

### 15. Pengujian Setter dengan Data Tidak Valid

Menguji validasi setter menggunakan data yang tidak valid.

| Uji | Atribut | Nilai | Hasil yang diharapkan |
|---|---|---|---|
| 1 | `persentase_sukses` | `150` | `ValueError` (di luar 0% - 100%) |
| 2 | `persentase_sukses` | `'Sangat Tinggi'` | `ValueError` (bukan angka) |
| 3 | `total_dispatch` | `-5` | `ValueError` (tidak boleh negatif) |
| 4 | `reputasi_reward` | `0` | `ValueError` (harus lebih dari 0) |

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

## Screenshot Output Program

### Bukti Abstract Class Tidak Dapat Diinstansiasi

![Bukti Abstract Class](Images/abstract_class.png)

### Polimorfisme (Override), Duck Typing, dan Operator Overloading

![Polimorfisme](Images/polimorfisme.png)

![Duck Typing](Images/duck_typing.png)

![Operator Overloading](Images/operator_overloading.png)

### Asosiasi, DIP, Komposisi, dan Agregasi

![Asosiasi](Images/asosiasi.png)

![DIP](Images/dip.png)

![Komposisi](Images/komposisi.png)

![Agregasi](Images/agregasi.png)

### Setter Valid dan Tidak Valid

![Setter Valid](Images/setter_valid.png)

![Setter Tidak Valid](Images/setter_tidak_valid.png)

------------------------------------------------------------------------------------------------------------------------------------------------

## Persyaratan Sistem

Untuk menjalankan program ini, pastikan sistem telah terinstal:

* **Python** versi 3.8 atau yang lebih baru.

------------------------------------------------------------------------------------------------------------------------------------------------

## Cara Menjalankan Program

1. Simpan kedua file berikut di folder yang sama:

```text
main.py
posttest3_2509106066_AryasatyaRakhaPhanyputa.py
```

2. Buka terminal, Command Prompt (CMD) atau Vs code.

3. Arahkan terminal ke folder tempat file `main.py` disimpan.

4. Jalankan program dengan perintah berikut:

```bash
python main.py
```

5. Saat program berjalan, tekan **Enter** untuk melanjutkan ke pengujian berikutnya. Terminal akan dibersihkan otomatis sebelum masuk ke bagian berikutnya.

------------------------------------------------------------------------------------------------------------------------------------------------