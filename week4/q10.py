fibonacci_numbers = [0, 1]
for i in range(2,11):
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
print(fibonacci_numbers)
even=list(filter(lambda x:x%2==0,fibonacci_numbers))
print(even)
odd=list(filter(lambda x:x%2!=0,fibonacci_numbers))
print(odd)
