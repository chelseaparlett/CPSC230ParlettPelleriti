# comparison
print("hello" == "hello")
print("help" == "hello")


print("apple" > "applet")

print("Mac" > "Mary")

print("apple" < "burrito")

print("a" > "A")

# methods

print("hello".upper())

# upper and lower
user_input = input("Please type a phrase: ")

print(user_input)
print(user_input.upper())
print(user_input.lower())

# isalpha, isdigit, isupper, islower

user_input_number = int(input("Please enter a number 0-100: "))

## instead try....
user_input_number = input("Please enter a number 0-100: ")

while not user_input_number.isdigit():
    print("that is not a number, silly!")
    user_input_number = input("Please enter a number 0-100: ")

user_input_number = int(user_input_number)

# shout
shout = input("Please shout something: ")

if not shout.isupper():
    print("I SAID SHOUT!")

# replace

bep = '''Whatcha gonna do with all that junk
All that junk inside your trunk
I'ma get get get get you drunk
Get you love drunk off my hump
My hump my hump my hump my hump my hump
My hump my hump my hump my lovely little lumps
'''

kidzBop = bep.lower()
kidzBop = kidzBop.replace("junk", "stuff").replace("hump", "pumps").replace("get", "make")
kidzBop = kidzBop.replace("lumps", "pumps").replace("drunk", "jump")
print(kidzBop)

# startswith
name = input("Please enter 'My name is' and then your name in French: ")

if name.lower().startswith("je m'appelle"):
    print("GREAT!")

strip
id_num = input("please enter your chapman id number: ")

id_num = id_num.strip()
print(id_num)

# .split()
sentence = "The quick brown fox jumps over the lazy dog"
print(sentence.split())

my_variable_name = "This_variable_name_is_so_long"

print(my_variable_name.split("_"))
