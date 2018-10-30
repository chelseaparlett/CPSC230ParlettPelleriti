#FILE I/O
# f = open("hp.txt", 'w')
# for i in range(0,10):
#     f.write("hello")
# f.close()

# def wordRid(word):
#     return word.replace(",", "").replace(")","").replace("(","").replace("'","").replace("?","")
#
# def wordtopig(str1):
#     str1 = str1.lower()
#     str1 = wordRid(str1)
#     if str1 == "\n":
#         return str1
#     elif "\n" in str1:
#         str1 = str1.replace("\n","")
#     #print(str1)
#     if str1[0] in 'AEIOUaeiou':
#         return str1 + "yay"
#     else:
#         return str1[1:] + str1[0] + "ay"

#--------------------------
# f = open("Song.txt",'r')
# for line in f:
#     new_l = line.split(" ")
#     new_line_str = []
#     for word in new_l:
#         x = wordtopig(word)
#         new_line_str.append(x)
#     k = " ".join(new_line_str)
#
#     print(k)
