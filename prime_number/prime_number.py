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


def next_prime(max_number_eval):
    """Generate the prime values from 2 to a max number

    Conditions:
    - Exception of 2, a prime number is not even, only evaluate not even values from 3
    """
    if max_number_eval <= 1:
        return
    else:
        yield 2

        for x in range(3, max_number_eval+1, 2):
            if eval_prim(x):
                yield x


def prime_numbers(max_number_eval=100):
    """
    List prime numbers for a values's range, by default the range is 100

    :param max_number_eval: range's limit
    :return: None
    """
    prime_numbers_list = list(next_prime(max_number_eval))
    print('The prime numbers from 2 to {} are:{}'.format(max_number_eval, prime_numbers_list))


if __name__ == '__main__':
    prime_numbers()

