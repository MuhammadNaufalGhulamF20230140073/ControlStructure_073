# membuat input untuk nilai n
n = int(input("Masukan Angka: "))

# dua angka pertama dari deret Fibonacci
a, b = 0, 1

# menampilkan deret Fibonacci sampai nilai n (angka yang kita masukan)
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
