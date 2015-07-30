#! /usr/bin/python
#
# mencari set faktorisasi
# suggested solution by jim geovedi
from itertools import product

# n adalah index dari x
n = 4
jumlah = 27

solve = lambda N: filter(lambda x: sum(x) == N, product(range(10), repeat=4))
hasil = solve(jumlah)
#print hasil
print "ada %d solusi permutasi" % len(hasil)

ke110 = hasil[110]
print ke110
print len(ke110)
