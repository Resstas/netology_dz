word = str(input("Введите слово: "))
wordLen = len(word)

if (wordLen % 2 == 0):
    letter = word[(wordLen // 2) - 1: (wordLen // 2) + 1]
else:
    letter = word[wordLen // 2]
print(letter)



