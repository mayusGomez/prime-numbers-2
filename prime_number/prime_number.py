""""List prime numbers from 2 to x number"""


def eval_prim(possible_prime):
    """
    Receive a number and return True if the number is prime o False otherwise

    Source: https://en.wikipedia.org/wiki/Primality_test
    This algorithm take on account that:
    - Prime number is natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers
    - A simple approach is evaluate "possible_prime % range(2,possible_prime)==0" but:
        - The factors to evaluate are 2 to sqrt(possible_prime)
        - All primes are of the form 6k ± 1

    :param possible_prime: number to evaluate
    :return: True or False
    """
    if possible_prime <= 1:
        return False
    elif possible_prime <= 3:
        return True
    elif possible_prime % 2 == 0 or possible_prime % 3 == 0:
        return False

    i = 5
    while i**2 <= possible_prime:
        if possible_prime % i == 0 or possible_prime % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_numbers(max_number_eval=100):
    """
    List prime numbers for a values's range, by default the range is 100

    Preconditions:
    - Exception of 2, a prime number is not even

    :param max_number_eval: range's limit
    :return: None
    """
    possibles_primes = (x for x in range(3, max_number_eval+1, 2))
    primes = [x for x in possibles_primes if eval_prim(x)]
    primes.insert(0, 2)
    print('The prime numbers from 2 to {} are:{}'.format(max_number_eval, primes))


if __name__ == '__main__':
    prime_numbers()
