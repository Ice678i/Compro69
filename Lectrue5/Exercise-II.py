def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(str(num))

    return ", ".join(primes)

print(generate_primes(10))
print(generate_primes(20))
print(generate_primes(1))
print(generate_primes(2))
