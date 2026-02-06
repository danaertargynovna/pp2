#1
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
#2
i = 0
while i < 8:
    i += 1
    if i == 5:
        continue
    print(i)
#3
word = "banana"
i = 0
while i < len(word):
    if word[i] == "a":
        i += 1
        continue
    print(word[i])
    i += 1
#4
values = [1, 0, 4, 0, 7]
i = 0
while i < len(values):
    if values[i] == 0:
        i += 1
        continue
    print(values[i])
    i += 1
