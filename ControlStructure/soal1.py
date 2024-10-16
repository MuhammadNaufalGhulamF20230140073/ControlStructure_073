# membuat input untuk memasukan angka
nilai = float(input("Masukan nilai siswa: "))

# menambahkan siswa berdasarkan kriteria persentase nilai
if nilai >= 90:
    print("Excellent performance")
elif nilai >= 80:
    print("Very Good performance")
elif nilai >= 70:
    print("Good performance")
elif nilai >= 60:
    print("Average performance")
# jika di bawah 60 
else:
    print("Performance needs improvement")
