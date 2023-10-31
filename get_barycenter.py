#!/usr/bin/python3
import sys

filename=str(sys.argv[0])
listatoms=[int(a) for a in sys.argv[1:]]
print('Fichier xyz : ', filename)
print("Atomes : ", listatoms)

fio = open(filename)

il=0
for l in fio.getlines():
    il=il+1
    if il in listatoms:
        x = l.split(l)[1]
        y = l.split(l)[2]
        z = l.split(l)[3]

print(x/len(listatoms),y/len(listatoms),z/len(listatoms))
