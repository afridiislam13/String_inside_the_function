def reverse_string():
    user_input = input("Enter a string: ")
    
    reversed_string = user_input[::-1]
    
    return reversed_string

result = reverse_string()
print("Reversed string:", result)

