import math

print("please enter a number: ")
number = int(input())

primes = []
for i in range(2, number+1):
    primes.append(i)

i = 2
# from 2 to square root of number
while(i <= int(math.sqrt(number))):
    # if number is in list, delete its multiples
    if i in primes:
        # j returns multiples of i starting from i*2
        for j in range(i*2, number+1, i):
            if j in primes:
                # delete if it's in the list
                primes.remove(j)
    i = i+1

print(primes)
if number in primes:
    print("Prime Number!")
else:
    print("Not a Prime Number!")

# for reference, prime numbers: {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
