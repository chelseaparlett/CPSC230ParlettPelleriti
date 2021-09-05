# string creation

s1 = 'Hello'
s2 = "Hello"
s3 = '''Hello'''

print(s1, s2, s3)

# whitespace

whitespace = "Hey \nHi \nHello \n ..."
print(whitespace)

whitespace2 = "Big\tStretch"
print(whitespace)

# strings as collections

my_string = "Hello Mother Hello Father"
print(my_string[0])

my_string2 = "My Name is: Chelsea"
print(my_string2[5])

hw = "Hello World!"
print(hw[4])


# slicing
print(my_string[0:5])

print(my_string2[12:])

print(my_string2[::-1])

print(hw[::-2])

print(my_string[::])

# operations
## add
print(1 + 1)

print('1' + '1')

## multiply

print(1 * 10)

print('1' * 10)

# in

name = "Chelsea"

print('e' in name)
print("j" in name)
print('c' in name)

print("Chels" in name)

# immutability
x = "hello"
print(x[0])

x[0] = "j"

x = "jello"
