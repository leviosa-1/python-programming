def count_vowels_and_consonants(string):
    # Initialize counters for vowels and consonants
    vowel_count = 0
    consonant_count = 0

    # Define a string containing all vowels (both uppercase and lowercase)
    vowels = "AEIOUaeiou"

    # Iterate through each character in the string
    for char in string:
        # Check if the character is an alphabet letter
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

# Input a string from the user
input_string = input("Enter a string: ")

# Call the count_vowels_and_consonants function to count vowels and consonants
vowels, consonants = count_vowels_and_consonants(input_string)

# Print the counts
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
