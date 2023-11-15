import sys

def char_to_binary(char):
    ascii_value = ord(char)
    binary_representation = format(ascii_value, '08b')
    return ascii_value, binary_representation

def word_to_binary(word):
    binary_representation = []
    for char in word:
        ascii_value, binary_char = char_to_binary(char)
        print(f"ASCII character value of '{char}' is {ascii_value}. Binary representation of '{char}' in a Byte is {binary_char}")
        binary_representation.append(binary_char)
    return ' '.join(binary_representation)

def get_results(word):
    return word_to_binary(word)

menu = int(input('Menu\n=====\n1. Character\n2. Word\nEnter your choice: '))

if menu == 1:
    char = input("Enter a Character: ")
    word = char
elif menu == 2:
    word = input("Enter a Word: ")
else:
    sys.exit()

print('\nResults\n========')

results = get_results(word)
print('Total: {0}'.format(results))
