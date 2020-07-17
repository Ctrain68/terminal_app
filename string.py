numbers = {0:"""
    000000
    00  00
    00  00
    00  00
    000000
""",1:"""
    1111
      11
      11
      11
    111111""",2:"""
    222222
         2
    222222
    2
    222222""",3:"""
    333333
        33
    333333
        33
    333333""",4:"""
    44  44
    44  44
    444444
        44
        44"""}

lst1 = []
for numb in numbers:

    lst1.append(numbers[numb])


print (lst1)

strings_by_column = [s.split('\n') for s in lst1]

# Group the split strings by line
# In this example, all strings are the same, so for each line we
# will have three copies of the same string.
strings_by_line = zip(*strings_by_column)

# Work out how much space we will need for the longest line of
# each multiline string
max_length_by_column = [
    max([len(s) for s in col_strings])
    for col_strings in strings_by_column
]

for parts in strings_by_line:
    # Pad strings in each column so they are the same length
    padded_strings = [
        parts[i].ljust(max_length_by_column[i])
        for i in range(len(parts))
    ]
    print(''.join(padded_strings))

