#! /usr/bin/python
from array import *
from random import randint

n = 4       # jumlah bolongan
jumlah = 27 # jumlah angka di bolongan di atas
holes=[(2,3), (3,5), (4,7), (5,9)]

def sumKTP():
#    data = raw_input('masukkan nomor KTP: ')
    data = "3204062010620003"

    sumdata = 0
    for i in data:
        if i.isdigit():
            sumdata +=  int(i)

    # print 'Sum = ', sumdata
    # format output with leading zero
    strsumdata = "%03d" % sumdata
#    print strsumdata
    return strsumdata

str_data = sumKTP()

# generate card with ranmdom numbers
endrows = 10 
endcols = 20 
my_array = [ [ 0 for i in range(endcols) ] for j in range(endrows) ]

def random_num():
    range_start = 0
    range_end = 9 
    return randint(range_start, range_end)

for i in range(len(my_array)):
   #print
   for j in range(len(my_array[i])):
       my_array[i][j] = random_num()
       #print my_array[i][j],

#replace the first 3 numbers in array with sum of KTP number
my_array[0][0] = int(str_data[0])
my_array[0][1] = int(str_data[1])
my_array[0][2] = int(str_data[2])

# memilih salah satu faktorisasi
from random import randint
from itertools import product

solve = lambda N: filter(lambda x: sum(x) == N, product(range(10), repeat=4))
hasil = solve(jumlah)
print "ada %d solusi permutasi" % len(hasil)
# pilih salah satu secara random
pilihan = randint(0,len(hasil)-1)

print "selecting:", pilihan, hasil[pilihan]

print "substituting"
for i in range(n):
   x = holes[i][0]
   y = holes[i][1]
   print holes[i],"=>",hasil[pilihan][i]
   # substituting conten
   my_array[x][y] = hasil[pilihan][i]

print "new card number",
for i in range(len(my_array)):
   print
   for j in range(len(my_array[i])):
       print my_array[i][j],

from qrcode import *
qr = QRCode(version=20, error_correction=ERROR_CORRECT_M)
#qr = QRCode(version=20, error_correction=ERROR_CORRECT_Q)
qr.add_data(my_array)
qr.make()

im = qr.make_image()
im.save("id.png")
