import os
from posttest3_2509106066 import (
    Hero, HeroCombat, HeroIntelligence, HeroMobility,
    Misi, Dispatcher, Agency,
    SilentNotifier, PanggilanBersaing, PanggilanPeretasan, proses_panggilan,
)

def lanjut():
    input("Tekan Enter untuk melanjutkan...")
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print("==========================================================")
    print("|                     DISPATCH HERO                      |")
    print("==========================================================")

    lanjut()
    print("==========================================================")
    print("|                       DATA HERO                        |")
    print("==========================================================")

    hero1 = HeroIntelligence("Invisigal", 85, 90, "Smart Glasses")
    hero2 = HeroCombat("Blonde Blazer", 90, 95, "Necklace Power")
    hero3 = HeroMobility("Coupe", 75, 85, 10)

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
    print("-" * 50)

    lanjut()
    print("==========================================================")
    print("|                UJI ABSTRACT CLASS (ABC)                |")
    print("==========================================================")
    try:
        dummy = Hero("Dummy", 1, 50)  
    except TypeError as e:
        print("[Bukti ABC] Tidak bisa instansiasi Hero:", e)

    lanjut()
    print("==========================================================")
    print("|               UJI POLIMORFISME (Override)              |")
    print("==========================================================")
    for hero in [hero1, hero2, hero3]:   # satu loop, perilaku berbeda
        hero.aksi_khusus()
    print("-" * 50)

    lanjut()
    print("==========================================================")
    print("|                     UJI DUCK TYPING                    |")
    print("==========================================================")
    proses_panggilan(PanggilanBersaing("Selamatkan bank", "Selamatkan sekolah"))
    proses_panggilan(PanggilanPeretasan("sistem keamanan gedung"))
    print("-" * 50)

    lanjut()
    print("==========================================================")
    print("|              UJI OPERATOR OVERLOADING                  |")
    print("==========================================================")
    print("__str__ -> lihat Uji Komposisi (print(log))")
    print(f"__lt__ : {hero1.nama} < {hero2.nama} ? {hero1 < hero2}")
    print("Hero terkuat (max):", max(hero1, hero2, hero3).nama)
    print("-" * 50)

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
    print("-" * 50)

    lanjut()
    print("==========================================================")
    print("|                    DATA DISPATCHER                     |")
    print("==========================================================")
    operator1 = Dispatcher("Player 1", "PASS-1234")
    operator2 = Dispatcher("Player 2", "PASS-5678", notifier=SilentNotifier())  # contoh DIP + duck typing

    print("Info Operator 1:")
    operator1.info_operator()
    print("-" * 50)
    print("Info Operator 2:")
    operator2.info_operator()

    print("-" * 50)
    print("Verifikasi Kode Akses:")
    print(f"Kode PASS-1234: {operator1.verif_access('PASS-1234')}")
    print(f"Kode SALAH: {operator1.verif_access('SALAH')}")
    print("-" * 50)

    lanjut()
    print("==========================================================")
    print("|                      UJI ASOSIASI                      |")
    print("==========================================================")
    operator1.dispatch_tim_hero([hero1, hero3], inc1)
    print("-" * 50)
    print("Status setelah dispatch:")
    hero1.tampilkan_stats()
    hero3.tampilkan_stats()
    print(f"Total dispatch: {operator1.total_dispatch}")
    print("-" * 50)

    lanjut()
    print("==========================================================")
    print("|              UJI DIP (Dependency Injection)            |")
    print("==========================================================")
    print("Operator 1 memakai ConsoleNotifier (default), operator 2 memakai SilentNotifier.")
    print("Kelas Dispatcher sama, notifier berbeda, tanpa mengubah Dispatcher.")
    print("-" * 50)
    print("Operator 2 dispatch misi INC-02:")
    operator2.dispatch_tim_hero([hero2], inc2)
    print("(Tidak ada output di atas karena SilentNotifier.) Riwayat pesan:")
    print(operator2.notifier.riwayat)
    print("-" * 50)

    lanjut()
    print("==========================================================")
    print("|                      UJI KOMPOSISI                     |")
    print("==========================================================")
    operator1.tampilkan_log()
    print("-" * 50)

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
    print("Jumlah Dispatcher:", len(agency.daftar_dispatcher))
    print("-" * 50)

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
    print("-" * 50)

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
    print("-" * 50)

    lanjut()
    print("==========================================================")
    print("|              Uji Data Setter Tidak Valid               |")
    print("==========================================================")
    try:
        print("[Uji 1] Persentase sukses = 150")
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
        print("\n[Uji 4] Reward = 0")
        inc2.reputasi_reward = 0
    except ValueError as e:
        print("[ERROR]", e)

    print("-" * 50)

    lanjut()
    print("==========================================================")
    print("|                   PROGRAM SELESAI                      |")
    print("==========================================================")