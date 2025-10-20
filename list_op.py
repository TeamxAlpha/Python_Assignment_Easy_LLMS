def list_operations(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    return total, average, maximum

def reverse_list(my_list):
    return my_list[::-1]

# Examples
numbers = [1, 5, 3, 8, 2]
my_list = ['a', 'b', 'c']

total, avg, max_val = list_operations(numbers)
print("Sum:", total)
print("Average:", avg)
print("Maximum:", max_val)

print("Reversed list:", reverse_list(my_list))
