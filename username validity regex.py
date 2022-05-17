import re



regexAlpha = re.compile(r'^(\w){10}$') #exactly 10 alphanumeric characters

regexUpper = re.compile(r'[A-Z]{2,}') #2 or more capitals

regexDigits = re.compile(r'[0-9]{3,}') #3 or more numbers

regexRepeat = regex = re.compile(r'(.+?)\1{1,}') #no repeats

regexList = [regexAlpha, regexUpper, regexDigits]

print('A username has to be exactly 10 alphanumeric characters long, have 2 or more capitals, 3 or more numbers and no repeating characters.')
print('Input a username:')
x = input()

sorted_char = sorted(x) # orders the username you inputteds with numbers first and then letters alphabetically 
y = "".join(sorted_char)

usernameMatch = 'Valid'
for reg in regexList:
    if reg.search(y) == None:
        usernameMatch = 'Invalid'
        
        break
    elif regexRepeat.search(y):
        usernameMatch = 'Invalid'
        break

print(usernameMatch)


                   
