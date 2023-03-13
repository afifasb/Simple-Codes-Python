#Program untuk mengetahui tingkat lapisan atmosfer

print("=================================")
print("PROGRAM ANALISIS LAPISAN ATMOSFER")
print("=================================")
print("")
print("1. Troposfer = 0 - 9 Km")
print("2. Stratosfer = 10 - 39 Km")
print("3. Mesosfer = 40 - 69 Km")
print("4. Termosfer = 70 - 399 Km")
print("5. Eksosfer = > 399 Km")
print("")

#Mengambil inputan dari user
inputTinggi = int(input("Masukkan tinggi lapisan atmosfer : "))
print("")

#Percabangan if-else untuk menentukan jenis atmosfer
if 0 <= inputTinggi < 10:
    print("Lapisan Troposfer")
elif 10 <= inputTinggi < 40:
    print("Lapisan Stratosfer")
elif 40 <= inputTinggi < 70:
    print("Lapisan Mesosfer")
elif 70 <= inputTinggi < 400:
    print("Lapisan Termosfer")
elif inputTinggi >= 400:
    print("Lapisan Eksosfer")
else:
    print("Inputan tidak valid")


print("")