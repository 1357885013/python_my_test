#!/usr/bin/python3

v = []
for i in range(3):
    v.append(int(input("int " + str(i + 1) + ":")))

v.sort()

for i in range(3):
    print(v[i])
