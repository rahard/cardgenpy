#! /usr/bin/python
# menjumlahkan angka nomor KTP

data = raw_input('masukkan nomor KTP: ')

sumdata = 0
for i in data:
   if i.isdigit():
	# print i
   	sumdata +=  int(i)

# print 'Sum = ', sumdata
# format output with leading zero

strsumdata = "%03d" % sumdata
print strsumdata
