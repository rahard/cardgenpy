#! /usr/bin/python
#
# mencari set subset sum

n=4      # x1 ... xn  or in array x0 ... x(n-1)
x = [0 for i in range(n)]
sum=27   # sum(x1 ... xn)
cell=((3,4), (2,3), (8,5), (7,1))

def sum(x,n):
   jumlah=0
   for i in range(n):
      jumlah=jumlah+x[i]
   return jumlah

for i in range(n):
   x[i]=x[i]+1
   print sum(x,n)
