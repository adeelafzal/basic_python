from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

is_even = lambda n : n % 2 == 0

double_it = lambda n : n * 2

sum_it = lambda a, b : a + b 

evens = list(filter(is_even, nums))
doubles = list(map(double_it, evens))
sum = reduce(sum_it, evens)


print("Evens", evens)
print("Doubles", doubles)
print("Sum", sum)