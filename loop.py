for i in range(2,5):
    print(i)
colors = ['red', 'green', 'blue']
for index, color in enumerate(colors):
    print(index, color)
number = [1,3,4,5]
for num, col in zip(colors,number):
    print(num, col)
data = {'Name':'Jon Doe', 'Index':2212}
for name, index in data.items():
    print(name, index)
i = 0
while i <= 10:
    if i == 5:
        i += 1
        continue
    if i == 9:
        break
    print(i)
    i += 1