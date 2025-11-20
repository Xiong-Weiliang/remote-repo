#!/usr/bin/env python3

def factorial(n: int) -> int:
    """Return n! for n >= 0."""
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    try:
        n = int(input("Enter a non-negative integer: ").strip())
    except ValueError:
        print("Invalid integer.")
        return
    if n < 0:
        print("Number must be non-negative.")
        return
    print(f"{n}! = {factorial(n)}")

if __name__ == "__main__":
    main()