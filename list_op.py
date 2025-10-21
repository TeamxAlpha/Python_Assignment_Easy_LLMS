def list_operations(numbers: int) -> tuple[int, float, int]:
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    return total, average, maximum

def reverse_list(my_list: list[object]) -> list[object]:
    reverse_list = []
    for i in range(len(my_list) -1 , -1, -1):
        reverse_list.append(my_list[i])
    return reverse_list

# Examples
numbers = [1, 5, 3, 8, 2]
my_list = ['a', 2, 'b', 'c']

total, avg, max_val = list_operations(numbers)
print("Sum:", total)
print("Average:", avg)
print("Maximum:", max_val)

print("Reversed list:", reverse_list(my_list))
