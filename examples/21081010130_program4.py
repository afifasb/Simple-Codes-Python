#Program untuk menghitung volume bangun ruang

#Fungsi untuk menghitung volume Kubus
def volumeKubus(sisiKubus):
    volume = sisiKubus * sisiKubus * sisiKubus
    return volume

#Fungsi untuk menghitung volume Balok
def volumeBalok(panjangBalok, lebarBalok, tinggiBalok):
    volume = panjangBalok * lebarBalok * tinggiBalok
    return volume

#Fungsi untuk menghitung volume Tabung
def volumeTabung(radiusTabung, tinggiTabung):
    phi = 3.14159265358979323846
    volume = (phi * int(radiusTabung) * int(radiusTabung) * int(tinggiTabung)) / 3
    return volume

#Fungsi untuk menghitung volume Bola
def volumeBola(radiusBola):
    phi = 3.14159265358979323846
    volume = (phi * int(radiusBola) * int(radiusBola) * int(radiusBola)) * 4 / 3
    return volume
    

print("======================================")
print("PROGRAM MENGHITUNG VOLUME BANGUN RUANG")
print("======================================")
print("")
print("1. Menghitung Volume Kubus")
print("2. Menghitung Volume Balok")
print("3. Menghitung Volume Tabung")
print("4. Menghitung Volume Bola")

while True:

    #User menginputkan menu pilihan
    print("")
    pilihanUser = int(input("Masukkan pilihan menu (1/2/3/4) = "))
    print("")

    #Menggunakan if-else untuk memanggil fungsi sesuai dengan menu inputan user
    if pilihanUser == 1:
        sisi = int(input("Masukkan sisi kubus : "))
        print("Volume Kubus = ", volumeKubus(sisi))

    elif pilihanUser == 2:
        panjang = int(input("Masukkan panjang Balok = "))
        lebar = int(input("Masukkan lebar Balok = "))
        tinggi = int(input("Masukkan tinggi Balok = "))
        print("Volume Balok = ", volumeBalok(panjang, lebar, tinggi))

    elif pilihanUser == 3:
        radius = float(input("Masukkan radius Tabung = "))
        tinggi = float(input("Masukkan tinggi Tabung = "))
        print("Volume Tabung = ", volumeTabung(radius, tinggi))
    
    elif pilihanUser == 4:
        radius = float(input("Masukkan radius Bola = "))
        print("Volume Bola = ", volumeBola(radius))

    else:
        print("Pilihan menu yang Anda masukkan tidak tersedia!")

    print("")
    hitungLagi = input("Apakah Anda ingin melakukan perhitungan kembali? (y/n) : ")
    if hitungLagi == "n" or hitungLagi == "no" or hitungLagi == "No" or hitungLagi == "NO":
        print("")
        print("Terima kasih telah menggunakan sistem kami!")
        break