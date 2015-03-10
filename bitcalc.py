#Calculate the number of bits required for the series who's sum is
# n(n+1)/2
# and to find the number of bits represented by some function

import math as m

def bits(number):
    return int(m.floor(m.log(number,2))+1)

def bitsum(number):
    x = 1
    n = 1
    while x <= number:
        n = n + m.floor(m.log(x,2))+1
        x = x + 1
    return int(n)

number = input('input a number: ')
print "The number of unsigned bits for the number is, ", bits(number)
print "The bits required to sum the numbers from 0 to this number is, ", bitsum(number)
