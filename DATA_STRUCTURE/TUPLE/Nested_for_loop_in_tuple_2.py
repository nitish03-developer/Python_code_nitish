a=((10,20,30),(40,50,60))
print(a[0])
print(a[1])

# WITHOUT INDEX

for r in a:
    for c in r:
        print(c)
    print()


#WITH INDEX

n=len(a)
for i in range(n):
    for j in range(len(a[i])):

        print(i,j,a[i][j])

    print()
