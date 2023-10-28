jumlah = int(input("Masukkan Tinggi Segitiga : "))
for i in range(jumlah, 0, -1):
    for j in range(jumlah - i):
        print('  ', end=' ')
    for k in range(i):
        print('*', end='  ')
    print()