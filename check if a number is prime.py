def is_prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # Any other even number is not prime
    if n % 2 == 0:
        return False

    # Check for factors from 3 to square root of n, skipping even numbers
    for i in range(3, int(n**0.5) + 1, 2):
        # If n is divisible by any of these, it's not prime
        if n % i == 0:
            return False

    # If no divisors found, n is prime
    return True

# Ask the user for input
num = int(input("Enter a number to check if it is prime: "))

# Call the function and print the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")