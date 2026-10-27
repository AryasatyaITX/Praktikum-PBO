from abc import ABC, abstractmethod

# ABSTRAKSI -> Abstract Base Class(ABC)
class Hero(ABC):
    total_hero = 0
    nama_agency = "Phoenix Agency"
    maksimal_tim_dispatch = 3

    def __init__(self, nama, power_level, persentase_sukses, status="Standby"):
        self._nama = nama            
        self._status = status        
        self.power_level = power_level
        self.persentase_sukses = persentase_sukses  
        Hero.total_hero += 1
        self.__id_hero = Hero.total_hero  

    @property
    def nama(self):
        return self._nama

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, nilai):
        self._status = nilai

    @property
    def persentase_sukses(self):
        return self.__persentase_sukses

    @persentase_sukses.setter
    def persentase_sukses(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)):
            raise ValueError(f"Persentase sukses {self._nama} harus berupa angka!")
        if nilai_baru < 0 or nilai_baru > 100:
            raise ValueError(f"Persentase sukses {self._nama} harus 0% - 100%!")
        self.__persentase_sukses = nilai_baru

    @property
    def tipe_hero(self):
        return getattr(self, "TIPE", "Unknown")

    @property
    def id_hero(self):
        return self.__id_hero

    def info_dasar(self):
        return (f"[{self.__id_hero}] Hero: {self._nama} | Tipe: {self.tipe_hero} | "
                f"Power: {self.power_level} | SR: {self.persentase_sukses}% | Status: {self._status}")

    # Operator Overloading dengan magic method __lt__ : membandingkan hero berdasarkan power level
    def __lt__(self, other):
        return self.power_level < other.power_level

    @classmethod 
    def ubah_maksimal_tim(cls, jumlah): 
        if jumlah > 0: 
            cls.maksimal_tim_dispatch = jumlah 
            print(f"[Berhasil] Maksimal tim dispatch diubah menjadi {jumlah} hero.") 
        else: 
            print("Gagal Maksimal tim harus lebih dari 0!.") 
 
    @staticmethod 
    def validasi_tipehero(tipe): 
        tipe_valid = ["Charisma", "Vigor", "Combat", "Mobility", "Intelligence"] 
        return tipe.capitalize() in tipe_valid 
    
    def beristirahat(self):
        if self._status != "Resting":
            print(f"[Info] {self._nama} tidak beristirahat (Status: {self._status})")
            return
        self._status = "Standby"
        print(f"[Berhasil] {self._nama} selesai istirahat -> Standby")

    @abstractmethod
    def tampilkan_stats(self):
        pass

    @abstractmethod
    def aksi_khusus(self):
        pass

# Inheritance dan LSP (Liskov Substitution Principle)
# Semua subclass Hero menepati kontrak Hero (tampilkan_stats & aksi_khusus diimplementasikan penuh,
# tidak ada method yang hanya melempar error), sehingga objek subclass bisa dipakai di mana pun Hero dipakai.
class HeroCombat(Hero):
    TIPE = "Combat"
    def __init__(self, nama, power_level, persentase_sukses, senjata, status="Standby"):
        super().__init__(nama, power_level, persentase_sukses, status)  
        self.senjata = senjata 

    def tampilkan_stats(self):  # overriding
        print(self.info_dasar() + f" | Senjata: {self.senjata}")

    def aksi_khusus(self):      # overriding
        print(f"{self.nama} menyerang menggunakan {self.senjata}!")


class HeroIntelligence(Hero):
    TIPE = "Intelligence"
    def __init__(self, nama, power_level, persentase_sukses, gadget, status="Standby"):
        super().__init__(nama, power_level, persentase_sukses, status)
        self.gadget = gadget  

    def tampilkan_stats(self):  # overriding
        print(self.info_dasar() + f" | Gadget: {self.gadget}")

    def aksi_khusus(self):      # overriding
        print(f"{self.nama} menganalisis situasi dengan gadget {self.gadget}!")


class HeroMobility(Hero):
    TIPE = "Mobility"
    def __init__(self, nama, power_level, persentase_sukses, speed_level, status="Standby"):
        super().__init__(nama, power_level, persentase_sukses, status)
        self.speed_level = speed_level  

    def tampilkan_stats(self):  # overriding
        print(self.info_dasar() + f" | Speed: {self.speed_level}")

    def aksi_khusus(self):      # overriding
        print(f"{self.nama} bergerak cepat dengan speed level {self.speed_level}!")

# OCP: HeroVigor ditambahkan sebagai subclass baru tanpa mengubah Hero maupun subclass lainnya.
class HeroVigor(Hero):
    TIPE = "Vigor"
    def __init__(self, nama, power_level, persentase_sukses, stamina, status="Standby"):
        super().__init__(nama, power_level, persentase_sukses, status)
        self.stamina = stamina  

    def tampilkan_stats(self):  # overriding
        print(self.info_dasar() + f" | Stamina: {self.stamina}")

    def aksi_khusus(self):      # overriding
        print(f"{self.nama} mempunyai stamina sebesar {self.stamina}!")

# DIP (Dependency Inversion Principle)
# Dispatcher bergantung pada abstraksi MissionEvaluator, bukan pada kelas konkret.
class MissionEvaluator(ABC):
    @abstractmethod
    def nilai(self, tim, misi):
        pass

# OCP (Open/Closed Principle): aturan penilaian baru cukup ditambah sebagai subclass baru
# dari MissionEvaluator, tanpa mengubah Dispatcher maupun penilai yang sudah ada.
# penilaian konkret ditambahkan lewat kelas baru
class TypeEvaluator(MissionEvaluator):
    def nilai(self, tim, misi):
        tipe_tim = [hero.tipe_hero for hero in tim]
        print(f"TypeEvaluator memeriksa tipe tim {tipe_tim} terhadap syarat misi {misi.syarat_tipe}")
        return all(syarat in tipe_tim for syarat in misi.syarat_tipe)

# penilaian baru, Class dan data pada Dispatcher tidak diubah.
class SuccessRateEvaluator(MissionEvaluator):
    def __init__(self, batas=90):
        self.batas = batas

    def nilai(self, tim, misi):
        rata_rata = sum(hero.persentase_sukses for hero in tim) / len(tim)
        # misi yang lebih sulit mendapatkan reward lebih besar tetapi menuntut persentase sukses lebih tinggi
        dibutuhkan = min(100, self.batas + misi.reputasi_reward // 50)
        print(f"SuccessRateEvaluator: rata-rata tim {rata_rata:.1f}%, dibutuhkan {dibutuhkan}%")
        return rata_rata >= dibutuhkan


# KOMPOSISI: DispatchLog dibuat dan dimiliki oleh Dispatcher (disimpan di __logs)
class DispatchLog:
    def __init__(self, nama_operator, nama_misi, sukses):
        self.nama_operator = nama_operator
        self.nama_misi = nama_misi
        self.sukses = sukses
        
# Operator Overloading: magic method __str__
    def __str__(self): 
        hasil = "SUKSES" if self.sukses else "GAGAL"
        return f"[LOG] {hasil} | Operator: {self.nama_operator} | Misi: {self.nama_misi}"

 
class Dispatcher:
    def __init__(self, nama_operator, kode_akses, penilai: MissionEvaluator = None):
        self.nama_operator = nama_operator
        self.__kode_akses = kode_akses  
        self.total_dispatch = 0         
        self.__logs = []  # KOMPOSISI: log dibuat dan dimiliki Dispatcher
        # DIP: penilai disuntikkan lewat constructor (dependency injection); TypeEvaluator hanya fallback jika tidak diberikan
        self.penilai = penilai if penilai is not None else TypeEvaluator()

    @property
    def total_dispatch(self):
        return self.__total_dispatch

    @total_dispatch.setter
    def total_dispatch(self, nilai):
        if nilai < 0:
            raise ValueError("total_dispatch tidak boleh negatif")
        self.__total_dispatch = nilai

    def verif_access(self, input_kode):
        return input_kode == self.__kode_akses

    def info_operator(self):
        print(f"Nama Operator: {self.nama_operator}")
        print(f"Total Dispatch: {self.total_dispatch}")
        print("Kode Akses: [PRIVATE]")

    # ASOSIASI
    def dispatch_tim_hero(self, tim_hero, misi):
        print(f"[DISPATCH] {self.nama_operator} memproses '{misi.nama_kejadian}'...")

        if len(tim_hero) < 1 or len(tim_hero) > Hero.maksimal_tim_dispatch:
            print("[Gagal] Jumlah hero tidak sesuai!")
            self.__logs.append(DispatchLog(self.nama_operator, misi.nama_kejadian, False))
            return

        for h in tim_hero:
            if h.status != "Standby":
                print(f"[Gagal] {h.nama} tidak Standby (status: {h.status})")
                self.__logs.append(DispatchLog(self.nama_operator, misi.nama_kejadian, False))
                return

        # OCP + LSP: Dispatcher hanya memanggil nilai(); penilai apa pun (TypeEvaluator,
        # SuccessRateEvaluator, atau yang baru) bisa dipakai tanpa mengubah baris ini.
        if not self.penilai.nilai(tim_hero, misi):
            print("[MISI GAGAL] Tim tidak memenuhi penilaian misi.")
            for h in tim_hero:
                h.status = "Resting"
            self.__logs.append(DispatchLog(self.nama_operator, misi.nama_kejadian, False))
            return

        self.total_dispatch += 1
        for h in tim_hero:
            h.status = "Resting"
        print("[MISI SUKSES] Tim berhasil!")
        self.__logs.append(DispatchLog(self.nama_operator, misi.nama_kejadian, True))

    def tampilkan_log(self):
        print(f"Log milik {self.nama_operator}:")
        for log in self.__logs:
            print(log)  # pakai magic method__str__
            

class Misi:
    batas_waktu_respon_detik = 60  
    def __init__(self, id_misi, nama_kejadian, lokasi, syarat_tipe, reputasi_reward):
        self.id_misi = id_misi
        self.nama_kejadian = nama_kejadian
        self.lokasi = lokasi
        self.syarat_tipe = syarat_tipe
        self.reputasi_reward = reputasi_reward  

    @property
    def reputasi_reward(self):
        return self.__reputasi_reward

    @reputasi_reward.setter
    def reputasi_reward(self, nilai):
        if nilai <= 0:
            raise ValueError("Reward harus lebih dari 0")
        self.__reputasi_reward = nilai

    def info_misi(self):
        print("ID:", self.id_misi)
        print("Nama:", self.nama_kejadian)
        print("Lokasi:", self.lokasi)
        print("Syarat tipe:", self.syarat_tipe)
        print("Reward:", self.reputasi_reward)

#AGREGASI
class Agency:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_hero = []        
        self.daftar_dispatcher = []  

    def tambah_hero(self, hero):
        self.daftar_hero.append(hero)

    def tambah_dispatcher(self, dispatcher):
        self.daftar_dispatcher.append(dispatcher)

# DUCK TYPING: punya method tangani().
class Competingcalls:
    def __init__(self, opsi_a, opsi_b):
        self.opsi_a = opsi_a
        self.opsi_b = opsi_b

    def tangani(self):
        print(f"Pilih satu: '{self.opsi_a}' atau '{self.opsi_b}'.")


class Hackcalls:
    def __init__(self, target):
        self.target = target

    def tangani(self):
        print(f"[HACKING] Tidak ada hero dikirim atau membantu hero, operator meretas {self.target}.")


def proses_panggilan(panggilan):
    # Satu fungsi untuk semua jenis panggilan: yang penting mempunyai method tangani()
    panggilan.tangani()