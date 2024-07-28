def reverse_string(input_string):
    reversed_str = ""
    for char in input_string:
        reversed_str = char + reversed_str
    return reversed_str

# Input a string from the user
original_string = input("Enter a string: ")

# Call the reverse_string function to reverse the string
reversed_string = reverse_string(original_string)

# Print the reversed string
print("Reversed string:", reversed_string)
