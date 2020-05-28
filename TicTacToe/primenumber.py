# prime_numbers = all(n for n in range(2, 1001) if (n % 1 == 0 and n % (n-1) == 0))
# prime_numbers = [n for n in range(2,1001) if all((n % 1==0) and (n % (n-1) != 0))]
prime_numbers = [n for n in range(2,1001) if all(n for i in range(2, n) if (n % i == 0))]
print(prime_numbers)

# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)