#Program selisih antara dua jarak

print("================================")
print("PROGRAM SELISIH ANTARA DUA JARAK")
print("================================")
print("")

#User memasukkan jarak pertama
print("Jarak Pertama")
jarakKm1 = int(input("Masukkan jarak pertama (dalam KM) = "))
jarakMtr1 = int(input("Masukkan jarak pertama (dalam Meter) = "))

#User memasukkan jarak kedua
print("")
print("Jarak Kedua")
jarakKm2 = int(input("Masukkan jarak kedua (dalam KM) = "))
jarakMtr2 = int(input("Masukkan jarak kedua (dalam Meter) = "))

#Konversi dari KM ke M
konvJarak1 = jarakKm1 * 1000
konvJarak2 = jarakKm2 * 1000

#Kalkulasi total jarak pertama dan kedua dalam satuan meter
totalJarak1 = konvJarak1 + jarakMtr1
totalJarak2 = konvJarak2 + jarakMtr2

#Menggunakan if else untuk menghitung selisih
if totalJarak1 > totalJarak2:
    selisihJarak = totalJarak1 - totalJarak2
else:
    selisihJarak = totalJarak2 - totalJarak1

#Menampilkan selisih jarak
print("")
print("=============")
print("SELISIH JARAK")
print("=============")
print("")
print ("Jarak pertama = ", totalJarak1, "Meter")
print ("Jarak kedua = ", totalJarak2, "Meter")
print("")
print("Selisih antara dua jarak = ", selisihJarak, "Meter")
print("")