from typing import List  # Import List from typing

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    if n < 2:
        return False
    sum_divisors = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors == n

def is_armstrong(n: int) -> bool:
    digits: List[int] = [int(d) for d in str(n)]  # Use List[int] instead of list[int]
    num_digits = len(digits)
    return sum(d ** num_digits for d in digits) == n

def digit_sum(n: int) -> int:
    return sum(int(d) for d in str(n))