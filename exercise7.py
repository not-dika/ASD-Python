import numpy as np
import exercise7m as md

arr = np.array([])
rg = int(input("Masukan Jumlah Siswa: "))
for i in range(rg):
    inp = int(input(f"Masukan nilai siswa ke-{i+1}: "))
    arr = np.append(arr, inp)
print(f"Nilai Rata-Rata Kelas: {md.avg(arr)}")
print(f"Nilai Tertinggi: {md.max(arr)}")
print(f"Nilai Terendah: {md.min(arr)}")
print(f"Jumlah Siswa Diatas Rata-Rata: {md.abv_avg(arr)}")