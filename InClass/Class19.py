#FILE I/O

#INTRODUCE TRY/EXCEPT---------------
#Try and Except---------------------------------
# Chapter 6.6
#
# print("NO ERROR HANDLING-------------------------")
# fn = int(input("what's your favorite number? "))
#
# #what could go wrong?
# #
# print("WHILE LOOP--------------------------------")
fn = input("what's your favorite number? ")
while not fn.isnumeric():
    fn = input("what's your favorite number? ")
fn = int(fn)
#
# # #how have we fixed it in the past?
# #
# #try/Except
# print("TRY EXCEPT #1--------------------------------")
# try:
#     fn = int(input("what's your favorite number? "))
# except:
#     print("That's not a number, I'll pretend you said 7.")
#     fn = 7
#
# # #or
# print("TRY EXCEPT #2--------------------------------")
# while True:
#     try:
#         fn = int(input("what's your favorite number? "))
#         break
#     except:
#         print("That's not a number")

#
# print("\n\nFILE ISSUES-----------------------------------")
#reader = open("Chelsea.txt", "r")
# #what can go wrong?
#
# try:
#     filename = input("filename: ")
#     reader = open(filename, "r")
# except:
#     print("YOU MESSED UP. GO CHECK YOUR FILE LOCATION.")

# while True:
#     try:
#         filename = input("filename: ")
#         reader = open(filename, "r")
#         break
#     except:
#         print("YOU MESSED UP. GO CHECK YOUR FILE LOCATION.")
#-------------------------------

f = open("hp.txt", 'a')
for i in range(0,10):
    f.write("hello")
f.close()

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
#
# f = open("Song.txt",'r')
#
# for line in f:
#     nL = line.split(" ")
#     pigList = []
#     for word in nL:
#         pigWord = wordtopig(word)
#         pigList.append(pigWord)
#     newLine = " ".join(pigList)
#     print(newLine)
#
# #--------------------------
# # f = open("Song.txt",'r')
# # for line in f:
# #     new_l = line.split(" ")
# #     new_line_str = []
# #     for word in new_l:
# #         x = wordtopig(word)
# #         new_line_str.append(x)
# #     k = " ".join(new_line_str)
# #
# #     print(k)
