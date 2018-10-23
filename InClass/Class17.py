# Function to check length of words
# def listStringCheck(L):
#     odds = []
#     for i in L:
#         if len(i)%2 ==1:
#             odds.append(i)
#     return odds

def lSC(L):
    odds = []
    for word in L:
        if len(word)%2 == 1:
            odds.append(word)
    return odds
k = ["List", "items"]

odds = listStringCheck(k)

print(odds)

#-----------------------------
# Function to remove vowels
# def vowelRemover(st):
#     for v in "aeiou":
#         st = st.replace(v,"")
#     return st

def vR(st):
    st = st.lower()
    for v in "aeiou":
        if v in st:
            st = st.replace(v,"")
    return st


novs = vR("elephants")
print(novs)
#why does nothing print?
#-----------------------------
