jumlah = int(input("Masukkan Tinggi Segitiga :"))
for i in range(jumlah):
    for j in range(i+1):
        print('*', end='  ')
    print()
for i in range(i, 0, -1):
    for j in range(i):
        print('*', end='  ')
    print()
