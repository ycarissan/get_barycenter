#!/usr/bin/python3
import sys

filename=str(sys.argv[1])
listatoms=[int(a) for a in sys.argv[2:]]
print('Fichier xyz : ', filename)
print("Atomes : ", listatoms)

fio = open(filename)

il=-2
x=0
y=0
z=0
for l in fio.readlines():
    il=il+1
    if il in listatoms:
        x = x + float(l.split()[1])
        y = y + float(l.split()[2])
        z = z + float(l.split()[3])

print(x/len(listatoms),y/len(listatoms),z/len(listatoms))
