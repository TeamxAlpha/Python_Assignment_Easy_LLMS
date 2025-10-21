def vowel_counter(string: str) ->int:
    vowels = "aeiou"
    string = string.lower()
    count = sum(1 for char in string if char in vowels)
    return count


print(vowel_counter("Hello, world!"))
