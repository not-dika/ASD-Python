nama = input('Masukan Nama:')
umur = int(input('Masukan Umur:'))
pekerjaan = input('Masukan Pekerjaan Orang Tua:')
penghasilan = int(input('Masukan Penghasilan '))
ipk = float(input('Masukan IPK:'))
list_pekerjaan = ["Pedagang","Nelayan","Petani"]

print(10*"-")
print('Nama:',nama)
print('Umur:',umur)
print('Pekerjaan ortu:',pekerjaan)
print('Penghasilan ortu:',penghasilan)
print('IPK:',ipk)
print(10*"=")
print("Selamat Anda Diterima!" if umur < 25 and penghasilan < 1000000 and ipk >= 2.7 and pekerjaan in list_pekerjaan else "Tetap semangat dan jangan putus asa")