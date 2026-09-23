class Hero: 
    total_hero = 0 
    nama_agency = "Phoenix Agency" 
    maksimal_tim_dispatch = 3   
 
    def __init__(self, nama, tipe_hero, power_level, status, persentase_sukses): 
        self.nama = nama 
        self.tipe_hero = tipe_hero 
        self.power_level = power_level 
        self.status = status 
        self.__persentase_sukses = persentase_sukses 
 
        Hero.total_hero += 1 
 
    @property 
    def persentase_sukses(self): 
        return self.__persentase_sukses  
 
    @persentase_sukses.setter 
    def persentase_sukses(self, nilai_baru): 
        if not isinstance(nilai_baru, (int, float)): 
            raise ValueError(f"Persentase sukses {self.nama} harus berupa angka!") 
        if nilai_baru < 0 or nilai_baru > 100: 
            raise ValueError(f"Persentase sukses {self.nama} harus berada di rentang 0% - 100%!") 
 
        self.__persentase_sukses = nilai_baru 
        print(f"[Sukses validasi] persentase sukses {self.nama} diperbarui menjadi {self.__persentase_sukses}%") 
 
    def tampilkan_stats(self): 
        print(f"Hero : {self.nama:<14} | Tipe : {self.tipe_hero:<12} | Power : {self.power_level:<3} | Success rate : {self.__persentase_sukses}% | Status : {self.status}") 
 
    def beristirahat(self): 
        if self.status != "Resting": 
            print(f"[Info] {self.nama} tidak beristirahat (Status saat ini : {self.status}).")   
            return 
        self.status = "Standby" 
        print(f"[Berhasil] {self.nama} selesai beristirahat! Status kembali menjadi 'Standby' dan siap bertugas") 
 
    @classmethod 
    def ubah_maksimal_tim(cls, jumlah): 
        if jumlah > 0: 
            cls.maksimal_tim_dispatch = jumlah 
            print(f"[Berhasil] Maksimal tim dispatch diubah menjadi {jumlah} hero.") 
        else: 
            print("Gagal Maksimal tim harus lebih dari 0!.") 
 
    @staticmethod 
    def validasi_tipehero(tipe): 
        tipe_valid = ["Charisma", "Vigor", "Power", "Mobility", "Intelligence"] 
        return tipe.capitalize() in tipe_valid 
 
 
class Dispatcher: 
    total_operator = 0 
    sistem_operasi = "Dispatch OS v2.0" 
    pusat_komando = "Central City Dispatch Tower" 
 
    def __init__(self, nama_operator, shift_aktif, stasiun_kerja, kode_akses, total_dispatch_awal=0): 
        self.nama_operator = nama_operator 
        self.shift_aktif = shift_aktif 
        self.stasiun_kerja = stasiun_kerja 
        self.__kode_akses = kode_akses 
        self.total_dispatch = total_dispatch_awal 
 
        Dispatcher.total_operator += 1 
 
    @property 
    def total_dispatch(self): 
        return self.__total_dispatch 
 
    @total_dispatch.setter 
    def total_dispatch(self, nilai): 
        if nilai < 0: 
            raise ValueError(f"Total dispatch operator {self.nama_operator} tidak boleh negatif!") 
         
        self.__total_dispatch = nilai 
 
    def verifikasi_kode_akses(self, input_kode): 
        return input_kode == self.__kode_akses 
 
    def dispatch_tim_hero(self, tim_hero: list, incident): 
        print(f"[DISPATCH CENTER] Operator {self.nama_operator} ({self.stasiun_kerja}) memproses panggilan '{incident.nama_kejadian}'...") 
 
        if len(tim_hero) < 1 or len(tim_hero) > Hero.maksimal_tim_dispatch: 
            print(f"  [Gagal] Jumlah hero dalam tim dispatch harus 1 sampai {Hero.maksimal_tim_dispatch} hero!") 
            return 
 
        for hero in tim_hero: 
            if hero.status != "Standby": 
                print(f"  [Gagal] {hero.nama} sedang tidak tersedia! (Status saat ini: {hero.status})") 
                return 
 
        tipe_tim = [h.tipe_hero for h in tim_hero] 
        kriteria_terpenuhi = all(syarat in tipe_tim for syarat in incident.syarat_tipe) 
 
        if not kriteria_terpenuhi: 
            print(f"  [MISI GAGAL] Kombinasi tipe tim {tipe_tim} tidak memenuhi kriteria misi {incident.syarat_tipe}!") 
            print("  [EFEK] Seluruh hero yang dikirim mengalami kelelahan dan masuk ke status 'Resting'!") 
            for hero in tim_hero: 
                hero.status = "Resting" 
            return 
 
        self.total_dispatch = self.total_dispatch + 1 
 
        nama_hero_str = ", ".join(h.nama for h in tim_hero) 
        print(f"  [MISI SUKSES] Tim ({nama_hero_str}) berhasil menyelesaikan misi '{incident.nama_kejadian}'!") 
        print("  [EFEK] Hero selesai bertugas dan sekarang masuk ke status 'Resting'.") 
 
        for hero in tim_hero: 
            hero.status = "Resting" 
 
    def info_operator(self): 
        print(f"Operator: {self.nama_operator} | Shift: {self.shift_aktif} | Meja: {self.stasiun_kerja} | Total Dispatch: {self.total_dispatch}") 
 
 
class Misi: 
    total_panggilan_masuk = 0 
    tingkat_prioritas_default = "High Alert" 
    batas_waktu_respon_detik = 60 
 
    def __init__(self, id_misi, nama_kejadian, lokasi, syarat_tipe, reputasi_reward): 
        self.id_misi = id_misi 
        self.nama_kejadian = nama_kejadian 
        self.lokasi = lokasi 
        self.syarat_tipe = syarat_tipe 
        self.__reputasi_reward = reputasi_reward 
 
        Misi.total_panggilan_masuk += 1 
 
    @property 
    def reputasi_reward(self): 
        return self.__reputasi_reward 
 
    @reputasi_reward.setter 
    def reputasi_reward(self, nilai_baru): 
        if nilai_baru <= 0: 
            raise ValueError(f"  [Gagal Validasi] Reputasi reward untuk '{self.nama_kejadian}' harus lebih dari 0!") 
 
        self.__reputasi_reward = nilai_baru 
        print(f"  [Sukses Validasi] Reward '{self.nama_kejadian}' diubah menjadi {self.__reputasi_reward} poin reputasi.") 
 
    def info_incident(self): 
        syarat_str = ", ".join(self.syarat_tipe) 
        print(f"[{self.id_misi}] Incident: {self.nama_kejadian:<22} | Lokasi: {self.lokasi:<10} | Kriteria Tipe: [{syarat_str}] | Reward: +{self.__reputasi_reward}") 
 
#main program 
print("=========================================================") 
print("|                    Dispatch Hero                      |") 
print("=========================================================") 
 
print("==========================================================") 
print("|                    Data Hero                           |") 
print("==========================================================") 
hero1 = Hero("Invisigal", "Intelligence", 85, "Standby", 90) 
hero2 = Hero("Blonde Blazer", "Power", 90, "Standby", 95) 
hero3 = Hero("Coupe", "Mobility", 75, "Standby", 85) 

print("Instance Method(Menampilkan Info/stats hero)") 
hero1.tampilkan_stats() 
hero2.tampilkan_stats() 

print("Class Attribute Hero:") 
print(f"  • Total hero: {Hero.total_hero}") 
print(f"  • Nama agency: {Hero.nama_agency}") 
print(f"  • Maksimal tim dispatch: {Hero.maksimal_tim_dispatch} hero") 
 
print("Static Method (Validasi Tipe Hero):") 
print(f"  • Tipe 'Intelligence' -> {Hero.validasi_tipehero('Intelligence')}") 
print(f"  • Tipe 'Cybernetic'   -> {Hero.validasi_tipehero('Cybernetic')}") 
 
print("Class Method (Mengubah Maksimal Tim Dispatch):") 
print(f"  • Maksimal tim sebelum diubah: {Hero.maksimal_tim_dispatch} hero") 
Hero.ubah_maksimal_tim(4) 
print(f"  • Maksimal tim setelah diubah: {Hero.maksimal_tim_dispatch} hero") 
 
print("==========================================================") 
print("|                    Data Misi                           |") 
print("==========================================================") 
inc1 = Misi("INC-01", "Penyelidikan Villain", "Downtown", ["Intelligence", "Mobility"], 150) 
inc2 = Misi("INC-02", "Kebakaran Gedung", "Sector 7", ["Power"], 80) 

print("Instance Method (Menampilkan Info misi)") 
inc1.info_incident() 
inc2.info_incident() 

print("Class Attribute Misi:") 
print(f"  • Total panggilan masuk: {Misi.total_panggilan_masuk}") 
print(f"  • Prioritas default: {Misi.tingkat_prioritas_default}") 
print(f"  • Batas waktu respon: {Misi.batas_waktu_respon_detik} detik") 
 
print("==========================================================") 
print("|                    Data Dispatcher                     |") 
print("==========================================================") 
operator1 = Dispatcher("Player 1", "Night Shift", "Meja Utama 01", "PASS-1234") 
print("Instance Method (Menampilkan Info operator)") 
operator1.info_operator() 

print("Class Attribute Dispatcher:") 
print(f"  • Total operator: {Dispatcher.total_operator}") 
print(f"  • Sistem operasi: {Dispatcher.sistem_operasi}") 
print(f"  • Pusat komando: {Dispatcher.pusat_komando}") 

print("Verifikasi Kode Akses:") 
print(f"  • Kode benar -> {operator1.verifikasi_kode_akses('PASS-1234')}") 
print(f"  • Kode salah -> {operator1.verifikasi_kode_akses('SALAH')}") 

operator1.dispatch_tim_hero([hero1, hero3], inc1) 

operator2 = Dispatcher("Player 2", "Day Shift", "Meja Utama 02", "PASS-5678") 
operator2.info_operator() 
 
print("Perubahan Status:") 
hero1.tampilkan_stats() 
operator1.info_operator() 
 
hero1.beristirahat() 
hero1.tampilkan_stats() 
 
print("==========================================================") 
print("|               Uji Data Setter Valid                    |") 
print("==========================================================") 
print(f"Success rate awal {hero2.nama}: {hero2.persentase_sukses}%") 
hero2.persentase_sukses = 98 
 
print(f"Reward awal '{inc2.nama_kejadian}': {inc2.reputasi_reward} poin") 
inc2.reputasi_reward = 120 
 
print("==========================================================") 
print("|               Uji Data Setter Tidak Valid              |") 
print("==========================================================") 
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