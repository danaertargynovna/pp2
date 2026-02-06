#1 
i = 0
while True:
    i += 1
    if i == 10:
        break
    print(i)

#2
while True:
    num = int(input("num"))
    if num == 0:
        break
#3
i = 1
while i < 10:
    if i % 4 == 0:
        break
    print(i)
    i += 1
#4
word = "python"
i = 0
while i < len(word):
    print(word[i])
    if word[i] == "o":
        break
    i += 1
#5
i = 1
while i <= 10:
    print(i)
    if i == 7:
        break
    i += 1
