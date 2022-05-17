import re

# You can enter in a lot of information and it will print a list of email addresses you include in what you have written.

regex = re.compile(r'\S{1,}@\S{1,}\.\S{1,}')

print('Please enter a brief description of yourself, including your email address.')
x = input()


print(regex.findall(x))



