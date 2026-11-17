import random
import sys
sys.set_int_max_str_digits(0) #remove limit for output
n = random.randint((2**11213)-1,(2**19937)-1) #23rd and 24th Mersenne primes cause yes
t = n
while (n != 1):
    print (n)
    if (n%2):
        n *= 3
        n += 1
    else:
        n //= 2
    for i in range(2):
        if (t%2):
            t *= 3
            t += 1
        else:
            t //= 2
    if t==n:
        if (n == 1):
            print(1)
        elif (n == 2):
            print(2)
            print(1)
        elif (n == 4):
            print(4)
            print(2)
            print(1)
        else:
            print("loop")
            print(n) #outputs number if loop found. by conjecture this part of the code should never be run
        break
