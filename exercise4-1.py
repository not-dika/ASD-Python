#while true, input nilai, then count avg and print all nilai
nilais = []
tot = 0
cnt = 0
while True:
    a = input('Masukan Nilai [Tulis "Selesai" jika Selesai]: ')
    if a.lower() != 'selesai':
      i = int(a)
      nilais.append(i)
      tot += i
      cnt += 1
      continue
    break
print('='*15)
print(f'Average of {cnt} entries: {tot/cnt}')
for index, nilai in enumerate(nilais):
    print(f'Index {index} : {nilai}')