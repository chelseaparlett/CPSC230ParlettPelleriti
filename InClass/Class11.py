#LISTs
# things_in_my_purse = ["gum","lipgloss","hand sanitizer","brush",
# "wallet","computer"]
#
# #your friends want gum
# gum = False
# for item in things_in_my_purse:
#     if item == "gum":
#         gum = True
# if gum:
#     print("here, have some gum")
# else:
#     print("sorry")
#---------------------------------------------------------------
# bag = []
# thing = "None"
#
# while thing != "":
#     thing = input("What would you like to bring? type item. Leave blank to stop. ")
#     bag.append(thing)
#     print("\nHere's a list of what you're bringing:")
#     for item in bag:
#         print(item)
#     print("\n")
#---------------------------------------------------------------
# #Club Penguin
# bad_words = ["heck", "fudge","crap","darn","geez", "ass"]
# chat = input("Type to Chat: ")
# Chat_has_bad = False
#
# # for word in bad_words:
# #     if word in chat:
# #         print("Oh my, please be more appropriate!")
# #         print("You cannot say " + word)
# #Club Penguin 2
#
# for word in bad_words:
#     if word in chat:
#         chat = chat.replace(word, "#"*len(word))
# print("YOU: ", chat)
#---------------------------------------------------------------
# sen = input("Give me a sentence: ")
# sen_List = sen.split(" ")
# print(sen_List)
# for word in sen_List:
#     if word.lower() == "books":
#         print("YOURE TALKING ABOUT BOOKS.")
