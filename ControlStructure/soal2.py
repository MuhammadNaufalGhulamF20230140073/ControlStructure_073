# membuat input untuk 3 angka
angka1 = float(input("Masukan angka pertama: "))
angka2 = float(input("Masukan angka kedua: "))
angka3 = float(input("Masukan angka ketiga: "))

# menggunakan if else untuk mencari angka terbesar di antara 3 angka yang kita input tadi
if angka1 >= angka2 and angka1 >= angka3:
    largest = angka1
elif angka2 >= angka1 and angka2 >= angka3:
    largest = angka2
else:
    largest = angka3

# mencetak angka terbesar
print("Angka terbesarnya adalah:", largest)
