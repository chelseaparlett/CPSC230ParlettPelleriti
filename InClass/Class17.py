# Function to check length of words
def listStringCheck(L):
    odds = []
    for i in L:
        if len(i)%2 ==1:
            odds.append(i)
    return odds

k = ["List", "item"]

odds = listStringCheck(k)

print(odds)

a = 7
a = "cloud"
#-----------------------------
# Function to remove vowels
def vowelRemover(st):
    for v in "aeiou":
        st = st.replace(v,"")
    return st


novs = vowelRemover("elephants")
print(novs)
#why does nothing print?
#-----------------------------
