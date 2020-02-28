n = int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors


list = make_divisors(n)
min = 1e13
for i in list:
    if n//i+i < min:
        min = n//i+i

print(min-2)