# level1_prime.py

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n (int): The number to check

    Returns:
        bool: True if prime, False otherwise
    """
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def main():
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is NOT a prime number.")


if __name__ == "__main__":
    main()