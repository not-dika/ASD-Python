nama = input("Nama Karyawan:")
jamKerja = int(input("Jam Kerja dalam satu hari:"))
tarifPerjam = int(input("Tarif per jam:"))
jumlahJam = jamKerja*20
gaji = jumlahJam*tarifPerjam
print(f"Gaji per bulan {nama} yang di terima adalah {gaji}")