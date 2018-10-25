List of Prime Numbers
==============================

This package list all the prime numbers between 2 to a parameter value, by default 100.
This is implemented like another option to next_prime() function of [gmpy2](https://gmpy2.readthedocs.io/en/latest/intro.html) 
library.

The function next_prime(max_number_eval) is a generator, only search primes of the form 6k ± 1. The prime numbers are not 
saved, then for evaluate if a number is prime, search for factors of the form 6k ± 1 and less than sqrt(max_number_eval)


Run
---
For execute this code:
- Create VirtualEnv and Install requirements
```
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```
- From python3 console
```python
from prime_number import prime_numbers
prime_numbers()    
```
- Can run as a generator too
```python
from prime_number import next_prime
for x in iter(next_prime(max_number_eval=100)):
   print(x)
```

Test
----
```
$ pytest
```

Requirements
------------
- python 3+
- pytest

References
----------

-   Wikipedia [Primary Test](https://en.wikipedia.org/wiki/Primality_test) 
-   Wikipedia [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) 
