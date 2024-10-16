# membuat input masukan untuk nilai n
n = int(input("Masukan angka: "))

# pengulangan(loop) untuk membentuk setengah piramid
for i in range(1, n + 1):
    print((str(i) + ' ') * i)
