# for

for i in range(0,10):
    print(i)

# evens

for i in range(0,10):
    if i%2 == 0:
        print("EVEN")
    else:
        print("ODD")

## humuhumunukunukuapuaa
h_count = 0
u_count = 0
m_count = 0
k_count = 0
a_count = 0
n_count = 0

for letter in "humuhumunukunukuapuaa":
    if letter == "h":
        h_count += 1
    elif letter == "u":
        u_count += 1
    elif letter == "m":
        m_count += 1
    elif letter == "k":
        k_count += 1
    elif letter == "a":
        a_count += 1
    elif letter == "n":
        n_count += 1
    else:
        print("What are you doing here?!")

# lists

nums = [1,2,3,4,5,6,7,8,9,10,11,12]

for n in nums:
    if n%3 == 0:
        print("this is divisible by 3")

names = ["Abby", "Billy", "Cathrine", "Devon","Elon", "Fred"]

for name in names:
    print("Hello " + name + "!")
