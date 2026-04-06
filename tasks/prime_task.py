"""Prime number check task."""


def is_prime(n: int) -> bool:
    """Return True if n is a prime number, else False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check possible factors of the form 6k +/- 1 up to sqrt(n).
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def _prompt_int(prompt: str) -> int:
    """Prompt until the user enters a valid integer."""
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a valid integer.")


def run_prime_checker() -> None:
    """CLI flow for the prime number check."""
    number = _prompt_int("Enter an integer to test for primality: ")
    result = is_prime(number)
    if result:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


if __name__ == "__main__":
    run_prime_checker()
