#! /usr/bin/python

sum = [0 for x in range(37)]

for p in range(10):
   for q in range(10):
      for r in range(10):
         for s in range(10):
            jumlah = p + q + r + s
            sum[jumlah] = sum[jumlah] + 1

for i in range(37):
   print i, ',' , sum[i]
