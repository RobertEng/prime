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
inputs = (100000, 100100, 100200, 100300, 100400, 100500, 100600, 100700)
jobs = [(input, job_server.submit(sum_primes, (input,), (isprime,), ("math",))) for input in inputs]
for input, job in jobs:
    print "Sum of primes below", input, "is", job()
 
print "Time elapsed: ", time.time() - start_time, "s"
job_server.print_stats()