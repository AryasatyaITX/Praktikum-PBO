import os
def lanjut():
    input("Tekan Enter untuk melanjutkan...")
    os.system("cls" if os.name == "nt" else "clear")

class Hero:
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

    def tampilkan_stats(self):
        print(f"Hero: {self._nama} | Tipe: {self.tipe_hero} | Power: {self.power_level} | SR: {self.persentase_sukses}% | Status: {self._status}")

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

class HeroCombat(Hero):
    TIPE = "Combat"
    def __init__(self, nama, power_level, persentase_sukses, senjata, status="Standby"):
        super().__init__(nama, power_level, persentase_sukses, status)  
        self.senjata = senjata 

    def tampilkan_stats(self):
        print(f"Hero: {self._nama} | Tipe: {self.tipe_hero} | Power: {self.power_level} | Senjata: {self.senjata} | SR: {self.persentase_sukses}% | Status: {self._status}")


class HeroIntelligence(Hero):
    TIPE = "Intelligence"
    def __init__(self, nama, power_level, persentase_sukses, gadget, status="Standby"):
        super().__init__(nama, power_level, persentase_sukses, status)
        self.gadget = gadget  

    def tampilkan_stats(self):
            print(f"Hero: {self._nama} | Tipe: {self.tipe_hero} | Power: {self.power_level} | Gadget: {self.gadget} | SR: {self.persentase_sukses}% | Status: {self._status}")


class HeroMobility(Hero):
    TIPE = "Mobility"
    def __init__(self, nama, power_level, persentase_sukses, speed_level, status="Standby"):
        super().__init__(nama, power_level, persentase_sukses, status)
        self.speed_level = speed_level  

    def tampilkan_stats(self):
            print(f"Hero: {self._nama} | Tipe: {self.tipe_hero} | Power: {self.power_level} | Speed: {self.speed_level} | SR: {self.persentase_sukses}% | Status: {self._status}")
 

class DispatchLog:
    def __init__(self, nama_operator, nama_misi, sukses):
        self.nama_operator = nama_operator
        self.nama_misi = nama_misi
        self.sukses = sukses

    def tampilkan(self):
        hasil = "SUKSES" if self.sukses else "GAGAL"
        print(f"[LOG] {hasil} | Operator: {self.nama_operator} | Misi: {self.nama_misi}")

 
class Dispatcher:
    def __init__(self, nama_operator, kode_akses):
        self.nama_operator = nama_operator
        self.__kode_akses = kode_akses  
        self.total_dispatch = 0         
        self.__logs = []                

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

        tipe_tim = [h.tipe_hero for h in tim_hero]
        for syarat in misi.syarat_tipe:
            if syarat not in tipe_tim:
                print(f"[MISI GAGAL] butuh {misi.syarat_tipe}, tim punya {tipe_tim}")
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
            log.tampilkan()
            

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

#main program 
os.system("cls" if os.name == "nt" else "clear")
print("==========================================================")
print("|                     DISPATCH HERO                      |")
print("==========================================================")

lanjut()
print("==========================================================")
print("|                       DATA HERO                        |")
print("==========================================================")

hero1 = HeroIntelligence("Invisigal",85,90,"Smart Glasses")
hero2 = HeroCombat("Blonde Blazer",90,95,"Necklace Power")
hero3 = HeroMobility("Coupe",75,85,10)

print("Data Hero:")
hero1.tampilkan_stats()
hero2.tampilkan_stats()
hero3.tampilkan_stats()
print("-" * 50)
print("Total Hero:", Hero.total_hero)
print("Nama Agency:", Hero.nama_agency)
print("Maksimal Tim:", Hero.maksimal_tim_dispatch)
print("-" * 50)
print("Uji Static Method:")
print("Tipe Intelligence:", Hero.validasi_tipehero("Intelligence"))
print("Tipe Cybernetic:", Hero.validasi_tipehero("Cybernetic"))
print("-" * 50)
print("Uji Class Method:")
print("Maksimal Tim sebelum:", Hero.maksimal_tim_dispatch)
Hero.ubah_maksimal_tim(4)
print("Maksimal Tim sesudah:", Hero.maksimal_tim_dispatch)

lanjut()
print("==========================================================")
print("|             Tampilkan Stats Hero(OVERRIDING)           |")
print("==========================================================")
print("Hero Intelligence:")
hero1.tampilkan_stats()
print("-" * 50)
print("Hero Combat:")
hero2.tampilkan_stats()
print("-" * 50)
print("Hero Mobility:")
hero3.tampilkan_stats()


lanjut()
print("==========================================================")
print("|                         DATA MISI                      |")
print("==========================================================")
inc1 = Misi("INC-01", "Penyelidikan Villain", "Downtown", ["Intelligence", "Mobility"], 150)
inc2 = Misi("INC-02", "Kebakaran Gedung", "Sector 7", ["Combat"], 80)

print("Misi 1:")
inc1.info_misi()
print("-" * 50)
print("Misi 2:")
inc2.info_misi()

print(f"Batas waktu respon: {Misi.batas_waktu_respon_detik} detik")

lanjut()
print("==========================================================")
print("|                    DATA DISPATCHER                     |")
print("==========================================================")
operator1 = Dispatcher("Player 1", "PASS-1234")
operator2 = Dispatcher( "Player 2", "PASS-5678")
print("Info Operator 1:")
operator1.info_operator()
print("-" * 50)
print("Info Operator 2:")
operator2.info_operator()
print("-" * 50)
print("Verifikasi Kode Akses:")
print(f"Kode PASS-1234: {operator1.verif_access('PASS-1234')}")
print(f"Kode SALAH: {operator1.verif_access('SALAH')}")

lanjut()
print("==========================================================")
print("|                      UJI ASOSIASI                      |")
print("==========================================================")
print("Dispatcher menggunakan Hero dan Misi.")
print("Misi:", inc1.nama_kejadian)
print("Tim:", hero1.nama, "dan", hero3.nama)

operator1.dispatch_tim_hero([hero1, hero3], inc1)
print("-" * 50)
print("Status setelah dispatch:")
hero1.tampilkan_stats()
hero3.tampilkan_stats()

print(f"Total dispatch: {operator1.total_dispatch}")


lanjut()
print("==========================================================")
print("|                      UJI KOMPOSISI                     |")
print("==========================================================")
print("=" * 50)
print("Log Dispatcher".center(50))
print("=" * 50)
operator1.tampilkan_log()


lanjut()
print("==========================================================")
print("|                     UJI AGREGASI                       |")
print("==========================================================")
agency = Agency("Phoenix Agency")
agency.tambah_hero(hero1)
agency.tambah_hero(hero2)
agency.tambah_hero(hero3)

agency.tambah_dispatcher(operator1)
agency.tambah_dispatcher(operator2)

print("Nama Agency:", agency.nama)
print("Jumlah Hero:", len(agency.daftar_hero))
print(f"Jumlah Dispatcher:{len(agency.daftar_dispatcher)}")

print("\nDaftar Hero:")
for hero in agency.daftar_hero:
    print("-", hero.nama)

print("\nDaftar Dispatcher:")
for dispatcher in agency.daftar_dispatcher:
    print("-", dispatcher.nama_operator)


lanjut()
print("==========================================================")
print("|                      STATUS HERO                       |")
print("==========================================================")
print("Sebelum pemulihan(resting):")
hero1.tampilkan_stats()
print("-" * 50)
print("Hero sedang Resting, sekarang dipulihkan ke Standby...")
hero1.beristirahat()
print("-" * 50)
print("Setelah pemulihan:")
hero1.tampilkan_stats()


lanjut()
print("==========================================================")
print("|                Uji Data Setter Valid                   |")
print("==========================================================")
print(f"Success rate awal {hero2.nama} : {hero2.persentase_sukses}")
hero2.persentase_sukses = 98
print(f"Success rate baru {hero2.nama} : {hero2.persentase_sukses}")
print("-" * 50)
print(f"Reward awal {inc2.nama_kejadian} : {inc2.reputasi_reward}")
inc2.reputasi_reward = 120
print(f"Reward baru {inc2.nama_kejadian} : {inc2.reputasi_reward}")

lanjut()
print("==========================================================")
print("|              Uji Data Setter Tidak Valid               |")
print("==========================================================")

try:
    print("\n[Uji 1] Persentase sukses = 150")
    hero2.persentase_sukses = 150
except ValueError as e:
    print("[ERROR]", e)

try:
    print("\n[Uji 2] Persentase sukses = 'Sangat Tinggi'")
    hero2.persentase_sukses = "Sangat Tinggi"
except ValueError as e:
    print("[ERROR]", e)

try:
    print("\n[Uji 3] Total dispatch = -5")
    operator1.total_dispatch = -5
except ValueError as e:
    print("[ERROR]", e)


try:
    print("[Uji 4] Reward = 0")
    inc2.reputasi_reward = 0
except ValueError as e:
    print("[ERROR]", e)

lanjut()
print("==========================================================")
print("|                   PROGRAM SELESAI                     |")
print("==========================================================")