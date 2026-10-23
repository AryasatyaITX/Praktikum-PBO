import os
from posttest3_2509106066 import ( Hero, HeroCombat, HeroIntelligence, HeroMobility, Misi, Dispatcher, Agency, SilentNotifier)

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
    hero1.aksi_khusus()
    hero2.aksi_khusus()
    hero3.aksi_khusus()

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

    lanjut()
    print("==========================================================")
    print("|                      UJI KOMPOSISI                     |")
    print("==========================================================")
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
    print("Jumlah Dispatcher:", len(agency.daftar_dispatcher))

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
        print("[Uji 1] Persentase sukses = 150\n")
        hero2.persentase_sukses = 150
    except ValueError as e:
        print("[ERROR]", e)

    try:
        print("[Uji 2] Persentase sukses = 'Sangat Tinggi'\n")
        hero2.persentase_sukses = "Sangat Tinggi"
    except ValueError as e:
        print("[ERROR]", e)

    try:
        print("[Uji 3] Total dispatch = -5\n")
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
    print("|                   PROGRAM SELESAI                      |")
    print("==========================================================")