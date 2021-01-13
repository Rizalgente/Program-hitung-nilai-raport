print('====PROGRAM HITUNG NILAI RAPORT====\n'.center(50))
while True:
    nilai_ujian1 = int(input("# Masukan Nilai Ujian Pertama: "))
    nilai_ujian2 = int(input("# Masukan Nilai Ujian Kedua: "))
    nilai_ujian3 = int(input("# Masukan Nilai Ujian Ketiga: "))

    hasil = (nilai_ujian1+nilai_ujian2+nilai_ujian3) / 3
    print("Total Nilai Yang Anda Dapatkan Adalah: {}".format(hasil))
    nilai = hasil
    if nilai >= 95:
        print("Nilai anda A\n")
    elif nilai >= 80:
        print("Nilai anda B\n")
    elif nilai >= 65:
        print("Nilai anda C\n")
    elif nilai >= 50:
        print("Nilai anda D\n")
        continue
    else:
        print("Nilai anda E\n")
