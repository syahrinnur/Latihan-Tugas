n = int(input("Tentukan Fibonnaci non rekursif dari: "))
a = 0
b = 1
s = 0

for x in range(n):
    print(s,end=" ")
    s = a + b
    b = a
    a = s