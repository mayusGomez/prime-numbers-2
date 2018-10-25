""""List prime numbers from 2 to x number"""


def eval_prim(possible_prime):
    """
    Receive a number and return True if the number is prime o False otherwise

    Source: https://en.wikipedia.org/wiki/Primality_test
    This algorithm take on account that:
    - Prime number is natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers
    - A simple approach is evaluate "possible_prime % range(2,possible_prime)==0" but:
        - The factors to evaluate are 2 to sqrt(possible_prime),
        - The factors to evaluate only must be primes, primes are of the form 6k ± 1
        - Not use Sieve of Eratosthenes(https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) for save memory

    :param possible_prime: number to evaluate
    :return: True or False
    """
    if possible_prime <= 1:
        return False
    elif possible_prime <= 3:
        return True
    elif possible_prime % 2 == 0 or possible_prime % 3 == 0:  # This values are primes
        return False

    i = 5  # first factor to evaluate, of the form 6(1)-1, second to evaluate is 7 of teh form 6(1)+1
    while i**2 <= possible_prime:
        if possible_prime % i == 0 or possible_prime % (i + 2) == 0:
            return False
        i += 6 # increment 6 for evaluate next possible prime factors
    return True


def next_prime(max_number_eval=100):
    """Generate the prime values from 2 to a max number

    Conditions:
    - 2 and 3 are prime, next only evaluate number of the form 6k ± 1
    - Start at 5 and 7, next to 11 and 13, next to 17 and 19, ...
    - To know if a number is prime call the function prime_eval(number)
    """
    if max_number_eval <= 1:
        return
    else:
        yield 2

    if max_number_eval > 2:
        yield 3

        k = 5
        while k <= max_number_eval:
            if eval_prim(k):
                yield k

            k += 2
            if k <= max_number_eval and eval_prim(k):
                yield k

            k += 4


def prime_numbers(max_number_eval=100):
    """
    List prime numbers for a values's range, by default the range is 100

    :param max_number_eval: range's limit
    :return: None
    """
    prime_numbers_list = list(next_prime(max_number_eval))
    print('The prime numbers from 2 to {} are:{}'.format(max_number_eval, prime_numbers_list))


if __name__ == '__main__':
    prime_numbers(503)

