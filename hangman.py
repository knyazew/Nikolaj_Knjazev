# from random import choice
# from datetime import datetime
#
#
# def save_result(result):
#     with open('result_hm.txt', 'a', encoding='utf-8') as f:
#         f.write(str(datetime.now()) + '\n')
#         f.write(result + '\n')
#
#
# print("H A N G M A N")
# name = input("Enter your name: ")
# print(f"Hello, {name}!")
# print("You have 8 attempts.")
# words = ["time",
#          "year",
#          "people",
#          "way",
#          "day",
#          "man",
#          "thing",
#          "woman",
#          "life",
#          "child",
#          "would",
#          "school",
#          "state",
#          "family",
#          "student",
#          "group",
#          "country",
#          "problem",
#          "hand",
#          "part",
#          "place",
#          "case",
#          "week",
#          "company",
#          "system",
#          "program",
#          "question",
#          "work",
#          "government",
#          "number",
#          "night",
#          "point",
#          "home",
#          "water",
#          "room",
#          "mother",
#          "area",
#          "money",
#          "story",
#          "fact",
#          "month",
#          "lot",
#          "right",
#          "study",
#          "book",
#          "eye",
#          "job",
#          "word",
#          "business",
#          "issue",
#          "side",
#          "kind",
#          "head",
#          "house",
#          "service",
#          "friend",
#          "father",
#          "power",
#          "hour",
#          "game",
#          "line",
#          "end",
#          "member",
#          "law",
#          "car",
#          "city",
#          "community",
#          "name",
#          "surname",
#          "president",
#          "team",
#          "minute",
#          "idea",
#          "kid",
#          "body",
#          "information",
#          "back",
#          "parent",
#          "face",
#          "others",
#          "level",
#          "office",
#          "door",
#          "health",
#          "person",
#          "art",
#          "war",
#          "history",
#          "party",
#          "result",
#          "change",
#          "morning",
#          "reason",
#          "research",
#          "girl",
#          "guy",
#          "moment",
#          "air",
#          "teacher",
#          "force",
#          "education",
#
#          ]
# count = 8
# while True:
#     command = input("Type \"play\" to play the game, \"exit\" to quit: ")
#     if command == "play":
#         word = choice(words)
#         solve = set(word)
#         hint = []
#         for i in range(len(word)):
#             hint.append("-")
#         entered_letter = set()
#         while count != 0:
#             if hint.count('-') == 0:
#                 print("")
#                 print("".join(hint))
#                 print("You guessed the word!")
#                 print("You survived!")
#                 save_result(f'{name} survived! Puzzled word is {word}.')
#                 count = 8
#                 break
#             else:
#                 print()
#                 print("".join(hint))
#                 letter = input("Input a letter: ")
#                 if len(letter) != 1:
#                     print("You should print a single letter")
#                 elif letter not in "abcdefghijklmnopqrstuvwxyz":
#                     print("It is not an ASCII lowercase letter")
#                 elif (
#                         letter in hint
#                         or letter in entered_letter
#                 ):
#                     print("You already typed this letter")
#                 elif letter in solve:
#                     for j in range(len(word)):
#                         if letter == word[j]:
#                             hint[j] = letter
#                             entered_letter.add(letter)
#                 else:
#                     print("No such letter in the word")
#                     entered_letter.add(letter)
#                     count -= 1
#         else:
#             print("")
#             print("You are hanged!")
#             print(f"Puzzled word is {word}.")
#             save_result(f'{name} hanged! Puzzled word is {word}.')
#             count = 8
#     elif command == "exit":
#         break
#     else:
#         print("Bad command!")
#         continue

a = list(map(str, input().split()))
b = []
for i in a:
    if i[len(i)-1] == 's':
        b.append(i)
print('_'.join(s for s in b))