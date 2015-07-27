#! /usr/bin/python
# sum number of ktp

data = raw_input('masukkan nomor KTP: ')
# print data
# print len(data)

#numbers = re.compile('\d+')
#baru = numbers.findall(data)
#print baru

sumdata = 0
for i in data:
   if i.isdigit():
	print i
   	sumdata +=  int(i)

print 'Sum = ', sumdata
