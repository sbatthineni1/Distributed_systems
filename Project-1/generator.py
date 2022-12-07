print("Enter your input - k value to generate sets: ")
k = int(input())
def calcN(k):
    n = k*(k-1) + 1
    return n

import itertools
def generate(n):
    total_numbers = set(range(1, n+1))
    subsets = list(itertools.combinations(total_numbers, k))
    common = []
    common.append(subsets[0])

    def common_member(a, b):
        a_set = set(a)
        b_set = set(b)

        if(len(a_set.intersection(b_set)) == 1):
            return True
        else:
            return False
   import math
import itertools

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return True
    else:
        return False
    # checking if k-1 is power of prime

# Array to store the prime numbers
is_prime = [True for i in range(10**6 + 1)]
primes =[]

# Function to mark the prime numbers using Sieve of Eratosthenes
def SieveOfEratosthenes(n):
    p = 2
    while (p * p <= n):
        # If prime[p] is not
        # changed, then it is a prime
        if (is_prime[p] == True):
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

# Function to check if the number can be represented as a power of prime
def power_of_prime(n):
    for i in primes:
        if n % i == 0:
            c = 0
            while n % i == 0:
                n//= i
                c += 1
            if n == 1:
                return (i, c)
            else:
                return (-1, 1)

# Driver Code
def check(n):
    #n = 49
    SieveOfEratosthenes(int(math.sqrt(n))+1)

    # Function Call
    num, power = power_of_prime👎
    if num > 1:
        return True
    else:
        return False

# calculating value of k for given n
k = math.ceil((1 + math.sqrt(1 - 4*(1-n))) / 2)
#is_power = check(k-1)
#print(is_power)

# generate node set 1 to n
node_set = set()
for i in range(1,n+1):
    node_set.add(i)

# generate all subsets of size k
node_subset = list(itertools.combinations(node_set, k))
#print(node_subset)

# generate all subsets of above subset
all_set = list(itertools.combinations(node_subset, k*(k-1) + 1))
print(all_set)
for i in all_set:
    j = 0
    while j < k*(k-1) - 1:
        l = j + 1
        if not common_member(i[j],i[l]):
            node_set.remove(i)
            break
        j += 1

for i in all_set:
    hash = {}
    for j in i:
        for x in j:
            if x not in hash:
                hash[x] = 1
            else:
                hash[x] += 1

    index = -999
    is_k = True
    for y in hash:
        if hash[y] != k:
            is_k = False
            break
    if is_k == True:
        print(i)
        break
