#!/usr/bin/python
# File: sum_primes.py
# Original author: Vitalii Vanovschi
# Desc: This program demonstrates parallel computations with pp module
# It calculates the sum of prime numbers below a given integer in parallel
# Parallel Python Software: http://www.parallelpython.com
 
import math
import time
import pp
 
 
def isprime(n):
    """Returns True if n is prime and False otherwise"""
    if n < 2:
        return False
    if n == 2:
        return True
    # no reason to go through all the numbers; the square root is as far as
    # we'll get anyway
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <= max:
        if n % i == 0:
            return False
        i += 1
    return True
 
 
def sum_primes(n):
    """Calculates sum of all primes below given integer n"""
    return sum([x for x in xrange(2, n) if isprime(x)])
 
# tuple of all parallel python servers to connect with, or "*", for
# autodiscovery
ppservers = ("*",)  # the comma is important!
 
# Creates jobserver with automatically detected number of workers
job_server = pp.Server(ppservers=ppservers)
 
print "Starting pp with", job_server.get_ncpus(), "workers"
 
start_time = time.time()
 
# The following submits 8 jobs and then retrieves the results
# inputs = (100000, 100100, 100200, 100300, 100400, 100500, 100600, 100700)
inputs = "171 40 133 169 75 8 73 187 195 48 89 151 54 63 90 33 68 81 118 24 159 7 146 15 4 156 31 134 35 109 62 158 95 143 12 74 77 17 126 139 128 101 39 100 14 172 167 49 175 141 145 19 130 170 148 179 165 157 83 161 153 121 105 46 85 164"
inputs = [int(i) + 100000 for i in inputs.split(' ')]

jobs = []
 
jobs.append(job_server.submit(sum_primes, (input,), (isprime,), ("math",)))
 
# gather results
for job in jobs:
    result = job()
    if result:
        break
 
if result:
    print result
else:
    print "Sorry, couldn't find anything."
    

# jobs = [(input, job_server.submit(sum_primes, (input,), (isprime,), ("math",))) for input in inputs]
# for input, job in jobs:
#     print "Sum of primes below", input, "is", job()
 
print "Time elapsed: ", time.time() - start_time, "s"
job_server.print_stats()





