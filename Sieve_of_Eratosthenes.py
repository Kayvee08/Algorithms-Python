#The sieve of Eratosthenes is one of the most efficient ways to find all primes smaller than n when n is smaller than 10 million
'''at the beginning we write down all numbers between 2 and n. We mark all proper multiples of 2 (since 2 is the
smallest prime number) as composite. A proper multiple of a number x, is a number greater than x and divisible by x.
Then we find the next number that hasn't been marked as composite, in this case it is 3. Which means 3 is prime,
and we mark all proper multiples of 3 as composite. The next unmarked number is 5, which is the next prime number,
and we mark all proper multiples of it. And we continue this procedure until we processed all numbers in the row.'''

def sieve(n):
    li=[True for i in range(2,n)]
    li.insert(0,False)
    li.insert(1,False)
    for i in range(2,n):
        if (li[i]):
            j=i
            while i*j <n:
                li[i*j]=False
                j+=1
    for i in range(2,n):
        if li[i]:
            print(i)
n = int(input())
print(f"All Prime Nos less than {n} are:")
sieve(n)


#TIME COMPLEXITY OF THIS ALGORITHM IS n*(log(log(n)))
