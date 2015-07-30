#! /usr/bin/python
#
# mencari set faktorisasi
# suggested solution by jim geovedi
from random import randint
from itertools import product

# n adalah index dari x
n = 4
jumlah = 27

solve = lambda N: filter(lambda x: sum(x) == N, product(range(10), repeat=4))
hasil = solve(jumlah)
#print hasil
print "ada %d solusi permutasi" % len(hasil)

# pilih salah satu secara random
pilihan = randint(0,len(hasil)-1)
print pilihan, hasil[pilihan]
