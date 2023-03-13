#Program menampilkan bentuk Belah Ketupat

print("========================================")
print("PROGRAM MENAMPILKAN BENTUK BELAH KETUPAT")
print("========================================")
print("")

lebarBangun = int(input("Masukkan lebar bangun Belah Ketupat = "))
print("")

#Menggunakan perulangan bersarang atau nested loop untuk menampilkan bentuk belah ketupat
for i in range(lebarBangun):
    for tampilSpasi in range(lebarBangun-i):
        print(" ", end="")
    for tampilBentuk in range(i + 1):
        print("o ", end="")
    print("")

for i in range(1, lebarBangun):
    for tampilSpasi in range(i + 1):
        print(" ", end="")
    for tampilBentuk in range(lebarBangun-i):
        print("o ", end="")
    print("")

print("")