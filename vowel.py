def vowel_counter(string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in string if char in vowels)
    return count

# Example
print(vowel_counter("Hello, world!"))  # Output: 3
