# membuat input untuk nilai n
n = int(input("Masukan Angka: "))

# membuat loop/perulangan untuk mencetak bilangan ganjil dari  1 sampai n (angka input yang kita masukan)
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)
