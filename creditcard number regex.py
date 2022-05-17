



import re

# A credit card number must begin with 4, 5, or 6
# It must be all digits
# It must be 16 digits long
# It may or may not have "-" between groups of 4 digits 

regex = re.compile(r'^[456](\d){3}-?(\d){4}-?(\d){4}-?(\d){4}$')
repeatRegex = re.compile(r'(\d)\1{3,}') #finding digits that are repeated 4 or more time. 
print('Input your credit card number:')
x = input()

if regex.search(x) != None:
    z = x.replace('-','')
    if repeatRegex.search(z) == None:
        print('Valid, that is a credit card number!')
    else:
        print('Invalid, that is not a credit card number!')
else:
    print('Invalid, that is not a credit card number!')

    
