n = int(input("Enter n: "))

divisors = []
start = 1
end = n - 1
while start <= end:
    if n % start == 0:
        divisors = divisors + [start]
    start += 1

divisors_sum = 0
for divisor in divisors:
    divisors_sum += divisor

    
if divisors_sum == n:
    print("The number is perfect")
else:
    print("The number is not perfect")
