#! /usr/bin/python
from array import *
from random import randint

def sumKTP():
#    data = raw_input('masukkan nomor KTP: ')
    data = "3204062010620003"

    sumdata = 0
    for i in data:
        if i.isdigit():
            # print i
            sumdata +=  int(i)

    print 'Sum = ', sumdata
    # format output with leading zero

    strsumdata = "%03d" % sumdata
    return strsumdata
#    print strsumdata

str_data = sumKTP()

endrows = 10 
endcols = 20 
my_array = [ [ 0 for i in range(endcols) ] for j in range(endrows) ]

def random_num():
    range_start = 0
    range_end = 9 
    return randint(range_start, range_end)

#print random_num()
#print "empty array"
#print my_array

for i in range(len(my_array)):
   print
   for j in range(len(my_array[i])):
       my_array[i][j] = random_num()
       print my_array[i][j],

#print "array with random numbers"
#print my_array

print
print str_data[0],
print str_data[1],
print str_data[2]

#replace the first 3 numbers in array with sum of KTP number
my_array[0][0] = str_data[0]
my_array[0][1] = str_data[1]
my_array[0][2] = str_data[2]

print my_array[0][0],
print my_array[0][1],
print my_array[0][2]

print
print "new card number",
for i in range(len(my_array)):
   print
   for j in range(len(my_array[i])):
       print my_array[i][j],

