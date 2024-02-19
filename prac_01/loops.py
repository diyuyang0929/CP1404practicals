for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

stars = int(input("Number of star: "))
for star in range(stars):
    print("*", end=' ')
print()

stars = int(input("Number of star: "))
for star in range(0, stars+1):
    print('*' * star)
print()

