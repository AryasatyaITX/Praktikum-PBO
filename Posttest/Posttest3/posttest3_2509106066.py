from abc import ABC, abstractmethod


# DIP: Dispatcher bergantung pada abstraksi Notifier, bukan kelas konkret.
# Objek notifier disuntikkan dari luar lewat constructor Dispatcher.
class Notifier(ABC):
    @abstractmethod
    def kirim(self, pesan):
        pass


class ConsoleNotifier(Notifier):
    def kirim(self, pesan):
        print(pesan)


class SilentNotifier(Notifier):
    def __init__(self):
        self.riwayat = []

    def kirim(self, pesan):
        self.riwayat.append(pesan)  # disimpan, tidak dicetak


# DUCK TYPING: punya method tangani().
class Competingcalls:
    def __init__(self, opsi_a, opsi_b):
        self.opsi_a = opsi_a
        self.opsi_b = opsi_b

    def tangani(self):
        print(f"[BERSAING] Pilih satu: '{self.opsi_a}' atau '{self.opsi_b}'.")


class Hackcalls:
    def __init__(self, target):
        self.target = target

    def tangani(self):
        print(f"[PERETASAN] Tidak ada hero dikirim, operator meretas {self.target}.")


def proses_panggilan(panggilan):
    # Satu fungsi untuk semua jenis panggilan: yang penting punya tangani()
    panggilan.tangani()


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

    # OPERATOR OVERLOADING: bandingkan hero berdasarkan power_level
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

# Inheritance
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
 

class DispatchLog:
    def __init__(self, nama_operator, nama_misi, sukses):
        self.nama_operator = nama_operator
        self.nama_misi = nama_misi
        self.sukses = sukses
        
# OPERATOR OVERLOADING: magic method __str__
    def __str__(self): 
        hasil = "SUKSES" if self.sukses else "GAGAL"
        return f"[LOG] {hasil} | Operator: {self.nama_operator} | Misi: {self.nama_misi}"

 
class Dispatcher:
    def __init__(self, nama_operator, kode_akses, notifier: Notifier = None):
        self.nama_operator = nama_operator
        self.__kode_akses = kode_akses  
        self.total_dispatch = 0         
        self.__logs = []
        self.notifier = notifier if notifier is not None else ConsoleNotifier()                

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
        self.notifier.kirim(f"[DISPATCH] {self.nama_operator} memproses '{misi.nama_kejadian}'...")

        if len(tim_hero) < 1 or len(tim_hero) > Hero.maksimal_tim_dispatch:
            self.notifier.kirim("[Gagal] Jumlah hero tidak sesuai!")
            self.__logs.append(DispatchLog(self.nama_operator, misi.nama_kejadian, False))
            return

        for h in tim_hero:
            if h.status != "Standby":
                self.notifier.kirim(f"[Gagal] {h.nama} tidak Standby (status: {h.status})")
                self.__logs.append(DispatchLog(self.nama_operator, misi.nama_kejadian, False))
                return

        tipe_tim = [h.tipe_hero for h in tim_hero]
        for syarat in misi.syarat_tipe:
            if syarat not in tipe_tim:
                self.notifier.kirim(f"[MISI GAGAL] butuh {misi.syarat_tipe}, tim punya {tipe_tim}")
                for h in tim_hero:
                    h.status = "Resting"
                self.__logs.append(DispatchLog(self.nama_operator, misi.nama_kejadian, False))
                return

        self.total_dispatch += 1
        for h in tim_hero:
            h.status = "Resting"
        self.notifier.kirim("[MISI SUKSES] Tim berhasil!")
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