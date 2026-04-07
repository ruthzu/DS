"""Count vowels in a string."""


def count_vowels(text: str) -> int:
    """Return the number of vowels in the given text."""
    vowels = set("aeiou")
    return sum(1 for ch in text.lower() if ch in vowels)


def run_vowel_counter() -> None:
    """CLI flow for counting vowels."""
    text = input("Enter a string: ").strip()
    total = count_vowels(text)
    print(f"Vowel count: {total}")


if __name__ == "__main__":
    run_vowel_counter()
