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
        line = l.strip()
        try:
            x = x + float(line.split()[1])
            y = y + float(line.split()[2])
            z = z + float(line.split()[3])
        except:
            print("Error in line\n{}\n{}".format(l,line))

print(x/len(listatoms),y/len(listatoms),z/len(listatoms))
