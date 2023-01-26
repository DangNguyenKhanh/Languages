# Check only character in alphabet a->z and A->Z  : Return boolean
name = "DangNguyenKhanh"
print(name.isalpha())           # True
name = "Dang Nguyen Khanh"
print(name.isalpha())           # False
print('hello123'.isalpha())     # False


# Check string is has only digit character
print('123'.isdigit())      # True
print('123a'.isdigit())     # False


# Check string only have normal character and digit character : Return boolean
print('123abc'.isalnum())      # True
print('123a@'.isalnum())       # False


# Check is upper string : Return boolean
print('HELLO'.isupper())    # True
print('Hello'.isupper())    # False


# Check is lower string : Return boolean
print('hello'.islower())    # True
print('Hello'.islower())    # False


# Check string if the first character is upper : Return boolean
print('Hello'.istitle())    # True
print('hello'.istitle())    # False


# Check is string start with a string given : Return boolean
print('Hello'.startswith('He'))    # True
print('hello'.startswith('He'))    # False


