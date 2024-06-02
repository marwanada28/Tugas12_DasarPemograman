from volume import bola, kubik, trapesium
from luas import lingkaran, persegi, segitiga
print("NAMA = MARWA NADA NAQIYYAH ")
print("NIM = 20230040179")
print("KELAS = TI23C")
print("MATA KULIAH = DASAR PEMOGRAMAN TUGAS SESI 12")


def main():
    print("Menu:")
    print("1. Luas Lingkaran")
    print("2. Luas Persegi")
    print("3. Luas Segitiga")
    print("4. Volume Bola")
    print("5. Volume Kubik")
    print("6. Volume Trapesium")
    print("7. Keluar")

    while True:
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            radius = float(input("Masukkan radius lingkaran: "))
            print("Luas Lingkaran:", lingkaran.luas_lingkaran(radius))
        elif pilihan == "2":
            sisi = float(input("Masukkan sisi persegi: "))
            print("Luas Persegi:", persegi.luas_persegi(sisi))
        elif pilihan == "3":
            alas = float(input("Masukkan alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            print("Luas Segitiga:", segitiga.luas_segitiga(alas, tinggi))
        elif pilihan == "4":
            radius = float(input("Masukkan jari-jari bola: "))
            print("Volume Bola:", bola.volume_bola(radius))
        elif pilihan == "5":
            sisi = float(input("Masukkan sisi kubik: "))
            print("Volume Kubik:", kubik.volume_kubik(sisi))
        elif pilihan == "6":
            atas = float(input("Masukkan alas atas trapesium: "))
            bawah = float(input("Masukkan alas bawah trapesium: "))
            tinggi = float(input("Masukkan tinggi trapesium: "))
            print("Volume Trapesium:",
                  trapesium.volume_trapesium(atas, bawah, tinggi))
        elif pilihan == "7":
            print("Thank You")
            break
        else:
            print("Opsi invalid, Try Again.")


if __name__ == "__main__":
    main()
