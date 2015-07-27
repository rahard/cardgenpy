#! /usr/bin/python
# sum number of ktp

import re

data = raw_input('masukkan nomor KTP: ')
# print data
# print len(data)

numbers = re.compile('\d+')
baru = numbers.findall(data)
print baru
