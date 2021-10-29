# basic try and except
num_not_found = True

num = input("Please give me a non-zero, positive integer: ")
while num_not_found:
    if not num.strip("-").isnumeric():
        print("oh no that's not a good number!")
        num = input("Please give me a non-zero, positive integer: ")
    elif int(num) <= 0:
        print("oh no that's not a good number!")
        num = input("Please give me a non-zero, positive integer: ")
    else:
        num = int(num)
        num_not_found = False

print(5/num)


# multiple exceptions



# multiple exceptions 2



# raising errors


# now


# raising errors 2



# finally
