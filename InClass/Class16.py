# SYNTAX

## define
def funct_name(arg1,arg2):
    b = "DO things" + arg1 + arg2
    return b + "."

##  call
c = "8"
c = int(c)
output = funct_name("hello", "no")

print(output)

#----------------------------------
def boringfn(n):
    n += 1
    print("In functions", n)
    return n
    print("hello")

k = 9

k = boringfn(k)
print("Out of Function",k)
#----------------------------------
def listChecker(to_check, list1, list2):
    if to_check in list1 and to_check in list2:
        return True
    else:
        return False
out = listChecker("a", ["a", "c"], ["bee", "g"])
print(out)

print(listChecker("a", ["a"], ["a"]))
#----------------------------------
